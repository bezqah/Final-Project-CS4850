# ast/ast_node_builder_factory.py

from .ast_node_type import ASTNodeType
from .ast_node_builder import ASTNodeBuilder

class ASTNodeBuilderFactory:
    @staticmethod
    def make_ast_node_builder(node_type: ASTNodeType) -> ASTNodeBuilder:
        return ASTNodeBuilder(node_type)
