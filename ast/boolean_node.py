from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class BooleanNode(ASTNode):
    """
    This class represents a boolean value in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def get_val(self) -> bool:
        """
        Get the value that this node represents.
        :return: True if label is "true", False otherwise.
        """
        return self.get_label() == "true"

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_boolean_node"):
            raise LuaError("Visitor missing visit_boolean_node method")
        return visitor.visit_boolean_node(self)
