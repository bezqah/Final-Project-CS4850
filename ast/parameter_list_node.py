from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError
from typing import List


class ParameterListNode(ASTNode):
    """
    This class represents a list of formal parameters in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def get_id_list(self) -> List[ASTNode]:
        """
        Get the list of formal parameters.
        :return: a list of ASTNode representing formal parameters
        """
        return self.children

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_parameter_list_node"):
            raise LuaError("Visitor missing visit_parameter_list_node method")
        return visitor.visit_parameter_list_node(self)
