from ast.binary_node import BinaryNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class SubNode(BinaryNode):
    """
    This class represents a binary subtraction operator in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_sub_node"):
            raise LuaError("Visitor missing visit_sub_node method")
        return visitor.visit_sub_node(self)
