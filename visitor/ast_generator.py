from antlr4 import TerminalNode, ParseTreeVisitor
from parser.LuaParser import LuaParser
from parser.LuaVisitor import LuaVisitor
from ast.ast_node_builder_factory import ASTNodeBuilderFactory, ASTNodeType
from util.lua_error import LuaError


class ASTGenerator(LuaVisitor):

    def __init__(self):
        self.factory = ASTNodeBuilderFactory()

    def visitExpression(self, ctx):
        node = None
        if ctx.getChildCount() == 3:
            child1 = ctx.getChild(1)
            if isinstance(child1, TerminalNode):
                token_type = child1.getSymbol().type
                op_map = {
                    LuaParser.MULT: ASTNodeType.MULTIPLY,
                    LuaParser.DIV: ASTNodeType.DIVIDE,
                    LuaParser.ADD: ASTNodeType.ADD,
                    LuaParser.SUB: ASTNodeType.SUB,
                    LuaParser.EQ: ASTNodeType.EQUAL,
                    LuaParser.NE: ASTNodeType.NOTEQUAL,
                    LuaParser.LT: ASTNodeType.LESS,
                    LuaParser.LE: ASTNodeType.LESSEQUAL,
                    LuaParser.GT: ASTNodeType.GREATER,
                    LuaParser.GE: ASTNodeType.GREATEREQUAL,
                    LuaParser.OR: ASTNodeType.OR,
                    LuaParser.AND: ASTNodeType.AND
                }
                if token_type in op_map:
                    node = self.factory.make_ast_node_builder(op_map[token_type])\
                        .add_child(ctx.getChild(0).accept(self))\
                        .add_child(ctx.getChild(2).accept(self))\
                        .build()
            else:
                node = self.factory.make_ast_node_builder(ASTNodeType.PAREN)\
                    .add_child(ctx.getChild(1).accept(self))\
                    .build()
        elif ctx.getChildCount() == 2:
            node = self.factory.make_ast_node_builder(ASTNodeType.NOT)\
                .add_child(ctx.getChild(1).accept(self))\
                .build()
        elif ctx.getChildCount() == 5:
            call_builder = self.factory.make_ast_node_builder(ASTNodeType.CALL)\
                .add_child(ctx.getChild(0).accept(self))
            call_builder = call_builder.add_child(
                ctx.getChild(3).accept(self) if ctx.getChild(3) else
                self.factory.make_ast_node_builder(ASTNodeType.ARGUMENTLIST).build()
            )
            node = call_builder.build()
        else:
            node = ctx.getChild(0).accept(self)
        return node

    def visitMethods(self, ctx):
        builder = self.factory.make_ast_node_builder(ASTNodeType.METHODLIST)
        for t in ctx.children:
            builder.add_child(t.accept(self))
        return builder.build()

    def visitExpressionList(self, ctx):
        builder = self.factory.make_ast_node_builder(ASTNodeType.BODY)
        for c in ctx.children:
            builder.add_child(c.accept(self))
        return builder.build()

    def visitDefaultCase(self, ctx):
        builder = self.factory.make_ast_node_builder(ASTNodeType.BODY)
        for i in range(2, ctx.getChildCount()):
            builder.add_child(ctx.getChild(i).accept(self))
        body = builder.build()
        test = self.factory.make_ast_node_builder(ASTNodeType.BOOLEAN).add_label("true").build()
        return self.factory.make_ast_node_builder(ASTNodeType.SWITCHCASE)\
            .add_child(test)\
            .add_child(body)\
            .build()

    def visitParamList(self, ctx):
        pl_builder = self.factory.make_ast_node_builder(ASTNodeType.PARAMETERLIST)
        for t in ctx.ID():
            pl_builder.add_child(self.factory.make_ast_node_builder(ASTNodeType.VARDEF)
                                 .add_label(t.getText()).build())
        return pl_builder.build()

    def visitVarRef(self, ctx):
        if ctx.getChildCount() == 1:
            return self.factory.make_ast_node_builder(ASTNodeType.VARREF)\
                .add_label(ctx.ID(0).getText()).build()
        class_ref = self.factory.make_ast_node_builder(ASTNodeType.VARREF)\
            .add_label(ctx.ID(0).getText()).build()
        method_ref = self.factory.make_ast_node_builder(ASTNodeType.VARREF)\
            .add_label(ctx.ID(1).getText()).build()
        return self.factory.make_ast_node_builder(ASTNodeType.METHODREF)\
            .add_child(class_ref).add_child(method_ref).build()

    def visitProgram(self, ctx):
        #print("DEBUG: Visiting program")
        #print(f"DEBUG: program ctx children = {[child.getText() for child in ctx.children]}")

        builder = self.factory.make_ast_node_builder(ASTNodeType.PROGRAM)
        for child in ctx.children:
            ast = child.accept(self)
            #print(f"DEBUG: child={child.getText()}, ast={ast}")
            if ast:
                builder.add_child(ast)

        program_node = builder.build()
        #print(f"DEBUG: AST = {program_node}")
        return program_node
    
    def visitConstantExp(self, ctx):
        if ctx.INTNUM():
            return self.factory.make_ast_node_builder(ASTNodeType.INTEGER).add_label(ctx.INTNUM().getText()).build()
        elif ctx.FLOATNUM():
            return self.factory.make_ast_node_builder(ASTNodeType.FLOAT).add_label(ctx.FLOATNUM().getText()).build()
        elif ctx.STRING():
            return self.factory.make_ast_node_builder(ASTNodeType.STRING).add_label(ctx.STRING().getText()).build()
        elif ctx.TRUE():
            return self.factory.make_ast_node_builder(ASTNodeType.BOOLEAN).add_label("true").build()
        elif ctx.FALSE():
            return self.factory.make_ast_node_builder(ASTNodeType.BOOLEAN).add_label("false").build()
        elif ctx.NULL():
            return self.factory.make_ast_node_builder(ASTNodeType.NULL).build()
        elif ctx.listExp():
            list_ctx = ctx.listExp()
            if list_ctx.getChildCount() == 2:  # LK RK
                return self.factory.make_ast_node_builder(ASTNodeType.LIST).build()
            else:
                builder = self.factory.make_ast_node_builder(ASTNodeType.LIST)
                # Skip the first and last children: [ and ]
                for i in range(1, list_ctx.getChildCount() - 1):
                    child = list_ctx.getChild(i)
                    if child.getText() == ',':
                        continue  # skip commas
                    item_ast = child.accept(self)
                    builder.add_child(item_ast) 
                return builder.build()
        else:
            raise LuaError(f"Unsupported constant expression: {ctx.getText()}")
        
    def visitIfExpr(self, ctx):
        condition = ctx.expression(0).accept(self)
        then_branch = ctx.expression(1).accept(self)
        else_branch = ctx.expression(2).accept(self)

        return self.factory.make_ast_node_builder(ASTNodeType.IF) \
            .add_child(condition) \
            .add_child(then_branch) \
            .add_child(else_branch) \
            .build()
    
    def visitIfExpr(self, ctx):
        test_expr = ctx.expression(0).accept(self)
        then_expr = ctx.expression(1).accept(self)
        else_expr = ctx.expression(2).accept(self)

        return self.factory.make_ast_node_builder(ASTNodeType.IF) \
            .add_child(test_expr) \
            .add_child(then_expr) \
            .add_child(else_expr) \
            .build()

    def visitSwitchExp(self, ctx):
        switch_builder = self.factory.make_ast_node_builder(ASTNodeType.SWITCH)
        case_list_builder = self.factory.make_ast_node_builder(ASTNodeType.SWITCHCASELIST)

        for case_ctx in ctx.switchCases().switchCase():
            # Only one expression in the case condition
            test_expr = case_ctx.expression().accept(self)

            result_builder = self.factory.make_ast_node_builder(ASTNodeType.BODY)
            for expr in case_ctx.expressionList().expression():
                result_builder.add_child(expr.accept(self))
            result_body = result_builder.build()

            case_builder = self.factory.make_ast_node_builder(ASTNodeType.SWITCHCASE)
            case_builder.add_child(test_expr)
            case_builder.add_child(result_body)

            case_list_builder.add_child(case_builder.build())

        default_ctx = ctx.defaultCase()
        default_builder = self.factory.make_ast_node_builder(ASTNodeType.BODY)
        for expr in default_ctx.expressionList().expression():
            default_builder.add_child(expr.accept(self))
        default_body = default_builder.build()

        switch_builder.add_child(case_list_builder.build())
        switch_builder.add_child(default_body)

        return switch_builder.build()
    
    def visitDefaultCase(self, ctx):
        body_builder = self.factory.make_ast_node_builder(ASTNodeType.BODY)
        for expr in ctx.expressionList().expression():
            body_builder.add_child(expr.accept(self))
        body = body_builder.build()

        # Create a "true" boolean expression as test for default
        test = self.factory.make_ast_node_builder(ASTNodeType.BOOLEAN).add_label("true").build()

        return self.factory.make_ast_node_builder(ASTNodeType.SWITCHCASE) \
            .add_child(test) \
            .add_child(body) \
            .build()

