from visitor.ast_visitor_interface import Visitor
from util.lua_error import LuaError
import re

def camel_to_snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


class SourceVisitor(Visitor):
    def __init__(self):
        pass

    def visit_argument_list_node(self, n):
        source = ", ".join(child.accept(self) for child in n.get_arguments())
        return source

    def visit_assign_node(self, n):
        return f"{n.get_lhs()} = {n.get_rhs().accept(self)}"

    def visit_body_node(self, n):
        return "\n".join(child.accept(self) for child in n.get_body()) + "\n"

    def visit_call_node(self, n):
        return f"{n.get_func().accept(self)}->({n.get_args().accept(self)})"

    def visit_class_node(self, n):
        return f"class {n.get_name()}{{\n\t{n.get_class_vars().accept(self)}\n{n.get_constructor().accept(self)}\n{n.get_methods().accept(self)}\n}}"

    def visit_switch_case_node(self, n):
        return f"case {n.get_test_expr().accept(self)}: {n.get_result_expr().accept(self)}"

    def visit_switch_node(self, n):
        cases_str = "".join(case.accept(self) for case in n.get_cases().get_switch_cases())
        default_str = n.get_default_case().accept(self)  # BodyNode.accept(visitor) will call visit_body_node
        return f"switch {{{cases_str}default:{default_str}}}"

    def visit_function_definition_node(self, n):
        return f"function {n.get_name()}({n.get_params().accept(self)}) {{\n{n.get_body().accept(self)}\n}}"

    def visit_float_node(self, n):
        return str(round(n.get_val(), 7))

    def visit_lambda_node(self, n):
        return f"lambda ({n.get_params().accept(self)}) {{\n{n.get_body().accept(self)}\n}}"

    def visit_if_node(self, n):
        return f"if {n.get_test_expr().accept(self)} then {n.get_then_expr().accept(self)} else {n.get_else_expr().accept(self)}endif"

    def visit_integer_node(self, n):
        return str(n.get_val())

    def visit_list_node(self, n):
        items = ", ".join(child.accept(self) for child in n.get_list())
        return f"[{items}]" if items else "[]"

    def visit_method_node(self, n):
        header = "init" if n.get_name() == "init" else f"method {n.get_name()}"
        return f"{header}({n.get_params().accept(self)}) {{\n{n.get_body().accept(self)}\n}}"

    def visit_method_ref_node(self, n):
        return f"{n.get_object_name()}.{n.get_method_name()}"

    def visit_create_node(self, n):
        return f"create {n.get_class_name()}"

    def visit_string_node(self, n):
        return n.get_label()

    def visit_var_ref_node(self, n):
        return n.get_id()

    def visit_let_node(self, n):
        return f"let {n.get_let_var_decls().accept(self)}{{ \n{n.get_body().accept(self)}\n}}\n"

    def visit_boolean_node(self, n):
        return str(n.get_val()).lower()

    def visit_add_node(self, n):
        return f"{n.get_left_operand().accept(self)} + {n.get_right_operand().accept(self)}"

    def visit_sub_node(self, n):
        return f"{n.get_left_operand().accept(self)} - {n.get_right_operand().accept(self)}"

    def visit_multiply_node(self, n):
        return f"{n.get_left_operand().accept(self)} * {n.get_right_operand().accept(self)}"

    def visit_divide_node(self, n):
        return f"{n.get_left_operand().accept(self)} / {n.get_right_operand().accept(self)}"

    def visit_not_node(self, n):
        return f"!{n.get_operand().accept(self)}"

    def visit_or_node(self, n):
        return f"{n.get_left_operand().accept(self)} || {n.get_right_operand().accept(self)}"

    def visit_and_node(self, n):
        return f"{n.get_left_operand().accept(self)} && {n.get_right_operand().accept(self)}"

    def visit_equal_node(self, n):
        return f"{n.get_left_operand().accept(self)} == {n.get_right_operand().accept(self)}"

    def visit_not_equal_node(self, n):
        return f"{n.get_left_operand().accept(self)} != {n.get_right_operand().accept(self)}"

    def visit_less_node(self, n):
        return f"{n.get_left_operand().accept(self)} < {n.get_right_operand().accept(self)}"

    def visit_less_equal_node(self, n):
        return f"{n.get_left_operand().accept(self)} <= {n.get_right_operand().accept(self)}"

    def visit_greater_node(self, n):
        return f"{n.get_left_operand().accept(self)} >= {n.get_right_operand().accept(self)}"

    def visit_greater_equal_node(self, n):
        return f"{n.get_left_operand().accept(self)} >= {n.get_right_operand().accept(self)}"

    def visit_paren_node(self, n):
        return f"({n.get_expr().accept(self)})"

    def visit_parameter_list_node(self, pln):
        pl = ", ".join(n.accept(self) for n in pln.get_id_list())
        return pl

    def visit_let_decl_node(self, n):
        return f"[{n.get_var()} {n.get_value_expr().accept(self)}]"

    def visit_let_decl_list_node(self, n):
        decls = "\n".join(ldn.accept(self) for ldn in n.get_decls())
        return f"(\n{decls}\n)"

    def visit_switch_case_list_node(self, n):
        return "\n".join(case.accept(self) for case in n.get_switch_cases()) + "\n"

    def visit_null_node(self, n):
        return "null"

    def visit_program_node(self, n):
        return "\n".join(an.accept(self) for an in n.get_program()) + "\n"

    def visit_instance_variable_list_node(self, n):
        return " ".join(ivn.accept(self) for ivn in n.get_vars())

    def visit_method_list_node(self, n):
        return "\n ".join(mn.accept(self) for mn in n.get_methods()) + "\n"

    def visit_var_def_node(self, n):
        return n.get_label()
    


    def visit(self, node):
        method_name = f'visit_{camel_to_snake(node.__class__.__name__)}'
        #print(f"[DEBUG] Visiting with method: {method_name}")  # ✅ Debug print
        visit_method = getattr(self, method_name, self.generic_visit)
        return visit_method(node)

    def generic_visit(self, node):
        raise PLp1Error(f"No visit method for {node.__class__.__name__}. "
                        f"Expected 'visit_{camel_to_snake(node.__class__.__name__)}'")


