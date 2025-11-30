from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class StringNode(ASTNode):
    """
    This class represents a string constant in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def get_string(self) -> str:
        """
        Get the value of the string.
        :return: the string label
        """
        return self.label

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_string_node"):
            raise LuaError("Visitor missing visit_string_node method")
        return visitor.visit_string_node(self)
