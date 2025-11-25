class Environment(dict):
    def __init__(self, next_env=None, vars=None, vals=None):
        super().__init__()
        self.next_env = next_env
        if vars is not None and vals is not None:
            self.add_to_map(vars, vals)

    def add_to_map(self, vars, vals):
        for name, value in zip(vars, vals):
            self[name] = value
    
    def put(self, name, value):
        """Store a single variable (or function) binding in this environment."""
        self[name] = value

    def lookup(self, name):
        env = self
        while env is not None:
            if name in env:
                return env[name]
            env = env.next_env
        raise KeyError(f"Undefined variable: {name}")
