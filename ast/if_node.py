from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class IfNode(ASTNode):
    """
    This class represents an if-expression in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def get_test_expr(self) -> ASTNode:
        """
        Get the expression being tested in the if-expression.
        """
        return self.get_child(0)

    def get_then_expr(self) -> ASTNode:
        """
        Get the expression to evaluate if the test is true.
        """
        return self.get_child(1)

    def get_else_expr(self) -> ASTNode:
        """
        Get the expression to evaluate if the test is false.
        """
        return self.get_child(2)

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_if_node"):
            raise LuaError("Visitor missing visit_if_node method")
        return visitor.visit_if_node(self)
