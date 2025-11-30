from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class FloatNode(ASTNode):
    """
    This class represents a floating-point constant in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def get_val(self) -> float:
        try:
            return float(self.label)
        except (TypeError, ValueError) as e:
            raise LuaError("Invalid float value in FloatNode", cause=e)

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_float_node"):
            raise LuaError("Visitor missing visit_float_node method")
        return visitor.visit_float_node(self)
