from ast.binary_node import BinaryNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class AddNode(BinaryNode):
    """
    This class represents an add-operation in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_add_node"):
            raise LuaError("Visitor missing visit_add_node method")
        return visitor.visit_add_node(self)
