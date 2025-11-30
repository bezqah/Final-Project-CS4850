from ast.ast_node_type import ASTNodeType  # Separate enum file recommended

# Importing all node classes
from ast.add_node import AddNode
from ast.and_node import AndNode
from ast.argument_list_node import ArgumentListNode
from ast.assign_node import AssignNode
from ast.body_node import BodyNode
from ast.boolean_node import BooleanNode
from ast.call_node import CallNode
from ast.create_node import CreateNode
from ast.divide_node import DivideNode
from ast.equal_node import EqualNode
from ast.float_node import FloatNode
from ast.function_definition_node import FunctionDefinitionNode
from ast.greater_equal_node import GreaterEqualNode
from ast.greater_node import GreaterNode
from ast.if_node import IfNode
from ast.instance_variable_list_node import InstanceVariableListNode
from ast.integer_node import IntegerNode
from ast.less_equal_node import LessEqualNode
from ast.less_node import LessNode
from ast.list_node import ListNode
from ast.method_list_node import MethodListNode
from ast.multiply_node import MultiplyNode
from ast.not_equal_node import NotEqualNode
from ast.not_node import NotNode
from ast.null_node import NullNode
from ast.or_node import OrNode
from ast.parameter_list_node import ParameterListNode
from ast.paren_node import ParenNode
from ast.string_node import StringNode
from ast.sub_node import SubNode
from ast.var_def_node import VarDefNode
from ast.var_ref_node import VarRefNode


class ASTNodeFactory:
    """
    Factory class to generate AST nodes based on the given ASTNodeType.
    """
    def make_ast_node(self, node_type: ASTNodeType):
        match node_type:
            case ASTNodeType.ADD: return AddNode()
            case ASTNodeType.AND: return AndNode()
            case ASTNodeType.ARGUMENTLIST: return ArgumentListNode()
            case ASTNodeType.ASSIGN: return AssignNode()
            case ASTNodeType.BODY: return BodyNode()
            case ASTNodeType.BOOLEAN: return BooleanNode()
            case ASTNodeType.CALL: return CallNode()
            case ASTNodeType.CREATE: return CreateNode()
            case ASTNodeType.DIVIDE: return DivideNode()
            case ASTNodeType.EQUAL: return EqualNode()
            case ASTNodeType.FLOAT: return FloatNode()
            case ASTNodeType.FUNCTIONDEF: return FunctionDefinitionNode()
            case ASTNodeType.GREATEREQUAL: return GreaterEqualNode()
            case ASTNodeType.GREATER: return GreaterNode()
            case ASTNodeType.IF: return IfNode()
            case ASTNodeType.INSTANCEVARLIST: return InstanceVariableListNode()
            case ASTNodeType.INTEGER: return IntegerNode()
            case ASTNodeType.LESSEQUAL: return LessEqualNode()
            case ASTNodeType.LESS: return LessNode()
            case ASTNodeType.LIST: return ListNode()
            case ASTNodeType.METHODLIST: return MethodListNode()
            case ASTNodeType.MULTIPLY: return MultiplyNode()
            case ASTNodeType.NOTEQUAL: return NotEqualNode()
            case ASTNodeType.NOT: return NotNode()
            case ASTNodeType.NULL: return NullNode()
            case ASTNodeType.OR: return OrNode()
            case ASTNodeType.PARAMETERLIST: return ParameterListNode()
            case ASTNodeType.PAREN: return ParenNode()
            case ASTNodeType.STRING: return StringNode()
            case ASTNodeType.SUB: return SubNode()
            case ASTNodeType.VARDEF: return VarDefNode()
            case ASTNodeType.VARREF: return VarRefNode()
            case _: raise ValueError(f"Invalid AST Node Type: {node_type}")
