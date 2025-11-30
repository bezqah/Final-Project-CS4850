from abc import ABC, abstractmethod
from typing import List, Optional, TYPE_CHECKING
from util.lua_error import LuaError

if TYPE_CHECKING:
    from visitor.ast_visitor_interface import Visitor

class ASTNode(ABC):
    def __init__(self):
        self.label: Optional[str] = None
        self.children: List['ASTNode'] = []

    def get_child(self, i: int) -> 'ASTNode':
        return self.children[i]

    def add_child(self, node: 'ASTNode'):
        self.children.append(node)

    def push_child(self, node: 'ASTNode'):
        self.children.insert(0, node)

    def set_child(self, i: int, node: 'ASTNode'):
        self.children[i] = node

    def get_label(self) -> Optional[str]:
        return self.label

    def set_label(self, label: str):
        self.label = label

    @abstractmethod
    def accept(self, visitor: 'Visitor') -> object:
        """Accept a visitor according to the visitor pattern."""
        raise LuaError("accept method not implemented")
