from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class CreateNode(ASTNode):
    """
    This class represents an object creation call in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def get_class_name(self) -> str:
        """
        Get the name of the class being instantiated.
        """
        return self.get_label()

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_create_node"):
            raise LuaError("Visitor missing visit_create_node method")
        return visitor.visit_create_node(self)
