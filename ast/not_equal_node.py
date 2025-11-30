from ast.binary_node import BinaryNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class NotEqualNode(BinaryNode):
    """
    This class represents a binary not-equal-to comparison operator in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_not_equal_node"):
            raise LuaError("Visitor missing visit_not_equal_node method")
        return visitor.visit_not_equal_node(self)
