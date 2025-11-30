from ast.binary_node import BinaryNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class MultiplyNode(BinaryNode):
    """
    This class represents a multiply binary operator in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_multiply_node"):
            raise LuaError("Visitor missing visit_multiply_node method")
        return visitor.visit_multiply_node(self)
