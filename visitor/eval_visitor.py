# --------------
# visior imports
# ---------------


# --------------
# Util Imports
# ---------------
from util.lua_error import LuaError
from util.value_factory import ValueFactory, ValueType
from util.environment import Environment
from util.list_value import ListValue
from util.int_value import IntValue
from util.float_value import FloatValue
from util.boolean_value import BooleanValue
#not used yet ---------------------------
from util.function import Function
from util.closure import Closure

# -----------------
# AST Imports
# -----------------



class EvalVisitor(Visitor):
    def __init__(self, env):
        self.env = env
        self.value_factory = ValueFactory()
        self.logging = True

    def numeric_compare(self, lop, rop, cmp_fn, symbol):
        # Convert Value → Python number
        def to_number(v):
            if isinstance(v, IntValue):
                return v.get_int()
            if isinstance(v, FloatValue):
                return v.getFloat()
            raise LuaError(f"Incompatible types: {v}")

        try:
            left_val = to_number(lop)
            right_val = to_number(rop)
            result = cmp_fn(left_val, right_val)   # run comparison
            return self.value_factory.make_value(ValueType.BOOL).add_value(result)
        except Exception:
            raise LuaError(f"Incompatible types: {lop} {symbol} {rop}")

            
    def apply_numeric_op(self, lop, rop, op, symbol):
        # Integer–Integer
        if isinstance(lop, IntValue) and isinstance(rop, IntValue):
            return self.value_factory.make_value(ValueType.INT).add_value(
                op(lop.get_int(), rop.get_int())
            )

        # Float–Int
        if isinstance(lop, FloatValue) and isinstance(rop, IntValue):
            return self.value_factory.make_value(ValueType.FLOAT).add_value(
                op(lop.getFloat(), rop.get_int())
            )

        # Int–Float
        if isinstance(lop, IntValue) and isinstance(rop, FloatValue):
            return self.value_factory.make_value(ValueType.FLOAT).add_value(
                op(lop.get_int(), rop.getFloat())
            )

        # Float–Float
        if isinstance(lop, FloatValue) and isinstance(rop, FloatValue):
            return self.value_factory.make_value(ValueType.FLOAT).add_value(
                op(lop.getFloat(), rop.getFloat())
            )

        raise LuaError(f"Incompatible types: {lop} {symbol} {rop}")


# -------------------------------------------------------------------------
# Arithmetic
# -------------------------------------------------------------------------

    def visit_AddNode(self, n):
        left = n.get_left_operand().accept(self)
        right = n.get_right_operand().accept(self)
        return self.apply_numeric_op(left, right, lambda a, b: a + b, "+")

    def visit_SubNode(self, n):
        left = n.get_left_operand().accept(self)
        right = n.get_right_operand().accept(self)
        return self.apply_numeric_op(left, right, lambda a, b: a - b, "-")

    def visit_MultiplyNode(self, n):
        left = n.get_left_operand().accept(self)
        right = n.get_right_operand().accept(self)
        return self.apply_numeric_op(left, right, lambda a, b: a * b, "*")

    def visit_DivideNode(self, n):
        left = n.get_left_operand().accept(self)
        right = n.get_right_operand().accept(self)

        # If both operands are integers → integer division
        if isinstance(left, IntValue) and isinstance(right, IntValue):
            return self.value_factory.make_value(ValueType.INT).add_value(
            left.get_int() // right.get_int()
        )

        # Otherwise → float division using apply_numeric_op
        return self.apply_numeric_op(left, right, lambda a, b: a / b, "/")


    def visit_ListNode(self, n):
        lv = ListValue()
        for node in n.getList():
            lv.append(node.accept(self))
        return lv


# ----------------------------------------------------------------------
# Comparison
# ----------------------------------------------------------------------

# start with a comparison driver?
# look at the latest project

    def visit_EqualNode(self, n):
        left = n.get_left_operand().accept(self)
        right = n.get_right_operand().accept(self)
        return self.numeric_compare(left, right, lambda a, b: a == b, "==")

    def visit_NotEqualNode(self, n):
        left = n.get_left_operand().accept(self)
        right = n.get_right_operand().accept(self)
        return self.numeric_compare(left, right, lambda a, b: a != b, "!=")


# -----------------------------------------------------------------------
# control
# -----------------------------------------------------------------------

    def visit_IfNode(self, n):
        raise NotImplementedError


# -----------------------------------------------------------------------
# Boolean Operators
# -----------------------------------------------------------------------
    
    def visit_OrNode(self, n):
        left = n.get_left_operand().accept(self)
        right = n.get_right_operand().accept(self)

        if isinstance(left, BooleanValue) and isinstance(right, BooleanValue):
            return self.value_factory.make_value(ValueType.BOOL).add_value(
                left.get_boolean() or right.get_boolean()
            )

        raise LuaError("Incompatible types for ||")


    def visit_AndNode(self, n):
        left = n.get_left_operand().accept(self)
        right = n.get_right_operand().accept(self)

        if isinstance(left, BooleanValue) and isinstance(right, BooleanValue):
            return self.value_factory.make_value(ValueType.BOOL).add_value(
                left.get_boolean() and right.get_boolean()
            )

        raise LuaError("Incompatible types for &&")

