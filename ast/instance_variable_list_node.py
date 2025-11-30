from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class InstanceVariableListNode(ASTNode):
    """
    This class represents a list of instance variables in a class definition in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def get_vars(self) -> list:
        """
        Get the list of instance variables.
        """
        return self.children

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_instance_variable_list_node"):
            raise LuaError("Visitor missing visit_instance_variable_list_node method")
        return visitor.visit_instance_variable_list_node(self)
