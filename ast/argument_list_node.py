from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class ArgumentListNode(ASTNode):
    """
    This class represents a list of arguments in a function call in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_argument_list_node"):
            raise LuaError("Visitor missing visit_argument_list_node method")
        return visitor.visit_argument_list_node(self)

    def get_arguments(self):
        """
        Returns a list of arguments to a function call
        """
        return self.children
