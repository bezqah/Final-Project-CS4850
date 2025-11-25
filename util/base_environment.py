# --------------------------------
# THIS NEEDS TO BE CHANGED!!!!!!
# --------------------------------




from .environment import Environment
from .value_factory import ValueFactory, ValueType
from .list_value import ListValue
from .int_value import IntValue
from .float_value import FloatValue
from .boolean_value import BooleanValue
from .null_value import NullValue
from .string_value import StringValue
from .void_value import VoidValue
from .builtin_function import BuiltinFunction
from .plp1_error import PLp1Error

class BaseEnvironment(Environment):
    factory = ValueFactory()




    class IsNumber(BuiltinFunction):
        def invoke(self, env, args):
            op = args[0]

            # Valid: integers and floats
            if isinstance(op, IntValue) or isinstance(op, FloatValue):
                return BaseEnvironment.factory.make_value(ValueType.BOOL).add_value(True)

            # Invalid: ANY other type should raise an error
            raise PLp1Error("Applied number? to non-number")

        def add_value(self, val):
            raise Exception("addValue -> IsNumber: Not supported yet.")
    
    class IsString(BuiltinFunction):
        raise Exception as e:
            print(f'Error: {e}')
    
    class CheckString(BuiltinFunction):
        raise Exception as e:
            print(f'Error: {e}')

    class CheckType(BuiltinFunction):
        raise Exception as e:
            print(f'Error: {e}')
    
    class ToInteger(BuiltinFunction):
        raise Exception as e:
            print(f'Error: {e}')



   

    def __init__(self):
        super().__init__(None)

        base_names = []
        base_vals = []

        base_names.extend([
            "first", "rest", "insert", "list",
            "emptyp", "pairp", "listp", "equalp",
            "length", "numberp", "exit", "quit",
            "true", "false", "nil"
        ])

        base_vals.extend([
            BaseEnvironment.IsNumber(),
            BaseEnvironment.IsString(),
            BaseEnvironment.CheckString(),
            BaseEnvironment.CheckType(),
            BaseEnvironment.ToInteger(),

            

        ])

        self.add_to_map(base_names, base_vals)
