from .value import Value

class ListValue(Value):
    def __init__(self):
        self.val = []

    def add_value(self, values):
        self.val.extend(values)
        return self

    def first(self):
        return self.val[0]

    def rest(self):
        new_list = list(self.val)
        if new_list:
            new_list.pop(0)
        lv = ListValue()
        lv.val = new_list
        return lv

    def insert(self, v):
        self.val.insert(0, v)
        return self

    def append(self, v):
        self.val.append(v)
        return self

    def length(self):
        return len(self.val)

    def is_null(self):
        return len(self.val) == 0

    def equals(self, other):
        return self._deep_equals(self, other)

    @staticmethod
    def _deep_equals(lv1, lv2):
        if lv1.is_null():
            return lv2.is_null()
        if lv2.is_null():
            return False

        f1 = lv1.first()
        f2 = lv2.first()

        if isinstance(f1, ListValue):
            if isinstance(f2, ListValue):
                return (ListValue._deep_equals(f1, f2) and
                        ListValue._deep_equals(lv1.rest(), lv2.rest()))
            else:
                return False

        if isinstance(f2, ListValue):
            return False

        return f1 == f2 and ListValue._deep_equals(lv1.rest(), lv2.rest())

    def __str__(self):
        s = "["
        for v in self.val:
            s += f"{v}, "
        if len(s) > 1:
            return s[:-2] + "]"
        else:
            return s + "]"
