from ast.ast_node import ASTNode
from util.lua_error import LuaError
from visitor.ast_visitor_interface import Visitor


class ListNode(ASTNode):
    """
    This class represents a list of values in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def get_list(self):
        return self.children

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_list_node"):
            raise LuaError("Visitor missing visit_list_node method")
        return visitor.visit_list_node(self)
