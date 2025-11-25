from .function import Function
from .plp1_error import PLp1Error
from .base_environment import Environment

class Closure(Function):
    def __init__(self, name, params, body, env):
        self.name = name
        self.params = params # list of AST param nodes
        self.body = body # AST body node
        self.env = env # the environment where this closure was created
    def __str__(self):
        return self.name if self.name else "#function"
    def get(self):
        return str(self)
    def invoke(self, env, args):
    
        # parameter count check
        if len(args) != len(self.params):
            raise PLp1Error("Invalid Function Call")
        # new environment extending closure's environment
        new_env = Environment(self.env)
        # Add each param name mapped to evaluated argument
        param_names = [p.get_label() for p in self.params]
        new_env.add_to_map(param_names, args)
        # Import EvalVisitor **inside function** to avoid circular import
        from visitor.eval_visitor import EvalVisitor
        return self.body.accept(EvalVisitor(new_env))
    
    def add_value(self, val):
        return self
