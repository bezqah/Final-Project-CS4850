from binary_node import BinaryNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class AndNode(BinaryNode):
    """
    This class represents an and-operation in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_and_node"):
            raise LuaError("Visitor missing visit_and_node method")
        return visitor.visit_and_node(self)
