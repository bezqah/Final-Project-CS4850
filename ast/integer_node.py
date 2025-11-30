from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class IntegerNode(ASTNode):
    """
    This class represents an integer constant in the AST of Lua.
    """

    def __init__(self):
        super().__init__()

    def get_val(self) -> int:
        """
        Get the integer value represented by this node.
        """
        return int(self.label)

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_integer_node"):
            raise LuaError("Visitor missing visit_integer_node method")
        return visitor.visit_integer_node(self)
