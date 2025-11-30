from ast.ast_node import ASTNode
from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError


class FunctionDefinitionNode(ASTNode):
    """
    This node represents a definition of a function in the AST for Lua.
    """

    def __init__(self):
        super().__init__()

    def get_name(self) -> str:
        """
        Get the name of the function being defined.
        """
        return self.label

    def get_params(self) -> ASTNode:
        """
        Get the list of formal parameters to the function.
        """
        return self.get_child(0)

    def get_body(self) -> ASTNode:
        """
        Get the body of the function.
        """
        return self.get_child(1)

    def accept(self, visitor: Visitor):
        if not hasattr(visitor, "visit_function_definition_node"):
            raise LuaError("Visitor missing visit_function_definition_node method")
        return visitor.visit_function_definition_node(self)
