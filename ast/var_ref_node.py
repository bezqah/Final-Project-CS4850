from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class VarRefNode(ASTNode):
    """
    This class represents a variable reference in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def get_id(self):
        return self.label

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_var_ref_node"):
            raise LuaError("Visitor missing visit_var_ref_node method")
        return visitor.visit_var_ref_node(self)
