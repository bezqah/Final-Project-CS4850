from enum import Enum

from .int_value import IntValue
from .float_value import FloatValue
from .boolean_value import BooleanValue
from .list_value import ListValue
from .null_value import NullValue
from .string_value import StringValue
from .void_value import VoidValue

class ValueType(Enum):
    INT = "INT"
    FLOAT = "FLOAT"
    BOOL = "BOOL"
    LIST = "LIST"
    NULL = "NULL"
    STRING = "STRING"
    VOID = "VOID"

class ValueFactory:

    def make_value(self, value_type):
        if value_type == ValueType.INT:
            return IntValue()
        if value_type == ValueType.FLOAT:
            return FloatValue()
        if value_type == ValueType.BOOL:
            return BooleanValue()
        if value_type == ValueType.LIST:
            return ListValue()
        if value_type == ValueType.NULL:
            return NullValue()
        if value_type == ValueType.STRING:
            return StringValue()
        if value_type == ValueType.VOID:
            return VoidValue()

        raise Exception(f"Unknown ValueType: {value_type}")
