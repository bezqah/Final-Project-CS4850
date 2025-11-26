















# --------------------------------
# THIS NEEDS TO BE CHANGED!!!!!!
# --------------------------------




from .environment import Environment
from .value_factory import ValueFactory, ValueType
from .list_value import ListValue
from .int_value import IntValue
from .float_value import FloatValue
from .boolean_value import BooleanValue
from .string_value import StringValue
from .void_value import VoidValue
from .builtin_function import BuiltinFunction
from .lua_error import LuaError

class BaseEnvironment(Environment):
    factory = ValueFactory()




    class IsNumber(BuiltinFunction):
        def invoke(self, env, args):
            op = args[0]

            # Valid: integers and floats
            if isinstance(op, IntValue) or isinstance(op, FloatValue):
                return BaseEnvironment.factory.make_value(ValueType.BOOL).add_value(True)

            # Invalid: ANY other type should raise an error
            raise LuaError("Applied number? to non-number")

        def add_value(self, val):
            raise Exception("addValue -> IsNumber: Not supported yet.")
    
    class IsString(BuiltinFunction):
        def invoke(self, env, args):
            op = args[0]

            if isinstance(op, StringValue):
                return BaseEnvironment.factory.make_value(ValueType.BOOL).add_value(True)
    
    class luaL_CheckString(BuiltinFunction):
        def invoke(self, env, args):
            #the 0 in args is a thread
            #the 1 is where to search on the stack
            raise NotImplementedError("checkstring builtin not implemented")



    class CheckType(BuiltinFunction):
        def invoke(self, env, args):
            op = args[0]
            
            if isinstance(op, IntValue):
                return "IntValue"
            elif isinstance(op, FloatValue):
                return "FloatValue"
            elif isinstance(op, StringValue):
                return "StringValue"
            elif isinstance(op, ListValue):
                return "ListValue"
            else:
                return "Unknown"
    
    class ToInteger(BuiltinFunction):
        def invoke(self, env, args):
            try:
                op = args[0]
                op = int(op)
                return BaseEnvironment.facory.make_value(ValueType.INT).add_value(op)
            except ValueError as e:
                raise LuaError(f"Error changing to int: {e}")



   

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
