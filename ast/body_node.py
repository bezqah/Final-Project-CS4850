from ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class BodyNode(ASTNode):
    """
    This class represents a sequence of AST nodes forming the body of another AST node in Lua.
    """

    def __init__(self):
        super().__init__()

    def get_body(self):
        """
        Get the nodes in the body.
        :return: List of ASTNode instances.
        """
        return self.children

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_body_node"):
            raise LuaError("Visitor missing visit_body_node method")
        return visitor.visit_body_node(self)
