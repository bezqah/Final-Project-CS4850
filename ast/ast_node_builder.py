from ast.ast_node_factory import ASTNodeFactory
from ast.ast_node_type import ASTNodeType  

class ASTNodeBuilder:
    """
    Builder class for constructing ASTNode instances in a step-by-step manner.
    """
    def __init__(self, node_type: ASTNodeType):
        self.node = ASTNodeFactory().make_ast_node(node_type)

    def add_label(self, label: str) -> 'ASTNodeBuilder':
        """
        Set the label of the AST node.
        """
        self.node.set_label(label)
        return self

    def add_child(self, child) -> 'ASTNodeBuilder':
        """
        Add a child node to the current AST node.
        """
        self.node.add_child(child)
        return self

    def push_child(self, child) -> 'ASTNodeBuilder':
        """
        Push a child node to the beginning (if different from `add_child` behavior).
        """
        self.node.push_child(child)
        return self

    def build(self):
        """
        Finalize and return the constructed AST node.
        """
        return self.node
