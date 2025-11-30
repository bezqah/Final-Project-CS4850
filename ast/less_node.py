from ast.binary_node import BinaryNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class LessNode(BinaryNode):
    """
    This class represents a binary less-than comparison node in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_less_node"):
            raise LuaError("Visitor missing visit_less_node method")
        return visitor.visit_less_node(self)
