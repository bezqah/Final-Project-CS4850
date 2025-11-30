from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class VarDefNode(ASTNode):
    """
    This class represents a variable definition in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_var_def_node"):
            raise LuaError("Visitor missing visit_var_def_node method")
        return visitor.visit_var_def_node(self)
