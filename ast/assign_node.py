from .ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class AssignNode(ASTNode):
    """
    This class represents an assignment expression in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_assign_node"):
            raise LuaError("Visitor missing visit_assign_node method")
        return visitor.visit_assign_node(self)

    def get_lhs(self) -> str:
        """
        Get the label of the left-hand side of the assignment.
        """
        return self.get_child(0).get_label()

    def get_rhs(self) -> ASTNode:
        """
        Get the right-hand side of the assignment.
        """
        return self.get_child(1)
