from ast.binary_node import BinaryNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class OrNode(BinaryNode):
    """
    This class represents a binary or-operator in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_or_node"):
            raise LuaError("Visitor missing visit_or_node method")
        return visitor.visit_or_node(self)
