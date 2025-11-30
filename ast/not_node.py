from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class NotNode(ASTNode):
    """
    This class represents a unary not-operator in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_not_node"):
            raise LuaError("Visitor missing visit_not_node method")
        return visitor.visit_not_node(self)

    def get_operand(self) -> ASTNode:
        """
        Get the operand to the not-operator.
        :return: the operand ASTNode
        """
        return self.get_child(0)
