from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class CallNode(ASTNode):
    """
    This class represents a function call in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_call_node"):
            raise LuaError("Visitor missing visit_call_node method")
        return visitor.visit_call_node(self)

    def get_func(self) -> ASTNode:
        """
        Get the function being called.
        """
        return self.get_child(0)

    def get_args(self) -> ASTNode:
        """
        Get the list of arguments in the function call.
        """
        return self.get_child(1)
