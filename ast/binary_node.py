from ast.ast_node import ASTNode


class BinaryNode(ASTNode):
    """
    This node represents a binary operator in the AST for Lua.
    """

    def get_left_operand(self) -> ASTNode:
        """Get the left operand of a binary operator"""
        return self.get_child(0)

    def set_left_operand(self, left_operand: ASTNode):
        """Set the left operand of a binary operator"""
        self.set_child(0, left_operand)

    def get_right_operand(self) -> ASTNode:
        """Get the right operand of a binary operator"""
        return self.get_child(1)

    def set_right_operand(self, right_operand: ASTNode):
        """Set the right operand of a binary operator"""
        self.set_child(1, right_operand)
