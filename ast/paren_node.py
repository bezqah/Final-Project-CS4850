from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class ParenNode(ASTNode):
    """
    This class represents a set of parentheses surrounding an expression in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def get_expr(self) -> ASTNode:
        """
        Get the expression surrounded by parentheses.
        :return: the child ASTNode inside the parentheses
        """
        return self.get_child(0)

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_paren_node"):
            raise LuaError("Visitor missing visit_paren_node method")
        return visitor.visit_paren_node(self)
