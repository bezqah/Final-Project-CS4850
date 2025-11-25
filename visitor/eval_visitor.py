# --------------
# visior imports
# ---------------


# --------------
# Util Imports
# ---------------


# -----------------
# AST Imports
# -----------------



class EvalVisitor(Visitor):
    def __init__(self, env):
        self.env = env
        self.value_factory = ValueFactory()
        self.logging = True

# -------------------------------------------------------------------------
# Arithmetic
# -------------------------------------------------------------------------

    def visit_AddNode(self, n):
        raise NotImplementedError
    
    def visit_SubNode(self, n):
        raise NotImplementedError

    def visit_MulNode(self, n):
        raise NotImplementedError

    def visit_DivNode(self, n):
        raise NotImplementedError

    def visit_ListNode(self, n):
        raise NotImplementedError


# ----------------------------------------------------------------------
# Comparison
# ----------------------------------------------------------------------

# start with a comparison driver?
# look at the latest project

    def visitEqualNode(self, n):
        raise NotImplementedError

    def visit_NotEqualNode(self, n):
        raise NotImplementedError


# -----------------------------------------------------------------------
# control
# -----------------------------------------------------------------------

    def visit_IfNode(self, n):
        raise NotImplementedError


# -----------------------------------------------------------------------
# Boolean Operators
# -----------------------------------------------------------------------
    def visit_NotNode(self, n):
        raise NotImplementedError
    
    def visit_OrNode(self, n):
        raise NotImplementedError
    
    def visit_AndNode(self, n):
        raise NotImplementedError

