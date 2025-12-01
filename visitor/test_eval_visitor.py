
import unittest
from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream
from parser.PLp1Lexer import PLp1Lexer
from parser.PLp1Parser import PLp1Parser
from visitor.ast_generator import ASTGenerator
from visitor.eval_visitor import EvalVisitor
from visitor.error_value import ErrorValue
from util.base_enviroment import BaseEnvironment
from util.value_factory import ValueFactory

def process_code(text, env):
    lexer = PLp1Lexer(InputStream(text))
    tokens = CommonTokenStream(lexer)
    parser = PLp1Parser(tokens)
    t = parser.program()
    ast = ASTGenerator().visitProgram(t)
    try:
        v = ast.accept(EvalVisitor(env))
        return v
    except Exception as ex:
        # Map all interpreter runtime errors to ErrorValue as Java version did
        ev = ErrorValue()
        try:
            return ev.add_value(str(ex))
        except Exception:
            # If add_value is not available, fall back to returning the raw error value
            return ev

class EvalVisitorTest(unittest.TestCase):
    logging = True

    def setUp(self):
        self.baseEnv = BaseEnvironment()

    def test_visit_add(self):
        if self.logging: print("testing: AddNode")
        self.assertEqual(process_code("2+3", self.baseEnv).get(), 5)

    def test_visit_add_float(self):
        if self.logging: print("testing: AddNodeF")
        self.assertEqual(process_code("2.0+3.1", self.baseEnv).get(), 5.1)

    def test_visit_add_tc1(self):
        if self.logging: print("testing: AddNodeTC1")
        v = process_code("'hi'+3", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_add_tc2(self):
        if self.logging: print("testing: AddNodeTC2")
        self.assertEqual(process_code("2.0+3", self.baseEnv).get(), 5.0)

    def test_visit_add_tc3(self):
        if self.logging: print("testing: AddNodeTC3")
        v = process_code("[1]+3", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_add_tc4(self):
        if self.logging: print("testing: AddNodeTC4")
        v = process_code("1+true", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_and(self):
        if self.logging: print("testing: AndNode")
        self.assertEqual(process_code("true & false", self.baseEnv).get(), False)

    def test_visit_and_tc1(self):
        if self.logging: print("testing: AndNodeTC1")
        v = process_code("true & 1", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_and_tc2(self):
        if self.logging: print("testing: AndNodeTC2")
        v = process_code("3.0 & false", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_arith(self):
        if self.logging: print("testing: Arith")
        self.assertEqual(process_code("4 + 5 * 6 - 10 / 2", self.baseEnv).get(), 29)

    def test_visit_arith_float(self):
        if self.logging: print("testing: Arithf")
        self.assertEqual(process_code("4.2 + 5.33 * 6.7 - 11.0 / 2.2", self.baseEnv).get(), 34.911)

    def test_visit_div(self):
        if self.logging: print("testing: DivideNode")
        self.assertEqual(process_code("2/3", self.baseEnv).get(), 0)

    def test_visit_div1(self):
        if self.logging: print("testing: DivideNode1")
        self.assertAlmostEqual(process_code("2.0/3.1", self.baseEnv).get(), 0.64516129, places=6)

    def test_visit_emptyp(self):
        if self.logging: print("testing: Empty")
        self.assertEqual(process_code("emptyp->([1,2,3])", self.baseEnv).get(), False)

    def test_visit_emptyp_true(self):
        if self.logging: print("testing: Emptyp")
        self.assertEqual(process_code("emptyp->([])", self.baseEnv).get(), True)

    def test_visit_emptyp_tc(self):
        if self.logging: print("testing: Emptytc")
        v = process_code("emptyp->(3)", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_eq(self):
        if self.logging: print("testing: EqualNode")
        self.assertEqual(process_code("2==3", self.baseEnv).get(), False)

    def test_visit_eqf(self):
        if self.logging: print("testing: EqualNodef")
        self.assertEqual(process_code("2.0==3.1", self.baseEnv).get(), False)

    def test_visit_equalp1(self):
        if self.logging: print("testing: Equal1")
        self.assertEqual(process_code("equalp->([2,3],[2,3])", self.baseEnv).get(), True)

    def test_visit_equalp2(self):
        if self.logging: print("testing: Equal2")
        self.assertEqual(process_code("equalp->([2,1],[2,3])", self.baseEnv).get(), False)

    def test_visit_equalpm1(self):
        if self.logging: print("testing: Equalm1")
        self.assertEqual(process_code("equalp->([2,[3,1]],[2,[3,1]]))", self.baseEnv).get(), True)

    def test_visit_equalpm2(self):
        if self.logging: print("testing: Equalm2")
        self.assertEqual(process_code("equalp->([2,[3,1]],[2,[3],1])", self.baseEnv).get(), False)

    def test_visit_equalpn1(self):
        if self.logging: print("testing: Equaln1")
        self.assertEqual(process_code("equalp->([1],[])", self.baseEnv).get(), False)

    def test_visit_equalpn2(self):
        if self.logging: print("testing: Equaln2")
        self.assertEqual(process_code("equalp->([],[1])", self.baseEnv).get(), False)

    def test_visit_equalptc1(self):
        if self.logging: print("testing: Equaltc1")
        v = process_code("equalp->(1,[3])", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_equalptc2(self):
        if self.logging: print("testing: Equaltc2")
        v = process_code("equalp->([1],3)", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_false(self):
        if self.logging: print("testing: False")
        self.assertEqual(process_code("false", self.baseEnv).get(), False)

    def test_visit_first(self):
        if self.logging: print("testing: First")
        self.assertEqual(process_code("first->([1,2,3])", self.baseEnv).get(), 1)

    def test_visit_firstn(self):
        if self.logging: print("testing: Firstn")
        v = process_code("first->([])", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_firsttc1(self):
        if self.logging: print("testing: Firsttc1")
        v = process_code("first->(3)", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_float(self):
        if self.logging: print("testing: FloatNode")
        self.assertEqual(process_code("3.01227", self.baseEnv).get(), 3.01227)

    def test_visit_ge(self):
        if self.logging: print("testing: GreaterEqualNode")
        self.assertEqual(process_code("2 >= 3", self.baseEnv).get(), False)

    def test_visit_ge_f(self):
        if self.logging: print("testing: GreaterEqualNodef")
        self.assertEqual(process_code("2.0 >= 3.1", self.baseEnv).get(), False)

    def test_visit_gt(self):
        if self.logging: print("testing: GreaterNode")
        self.assertEqual(process_code("2 > 3", self.baseEnv).get(), False)

    def test_visit_gt_f(self):
        if self.logging: print("testing: GreaterNodef")
        self.assertEqual(process_code("2.0 > 3.1", self.baseEnv).get(), False)

    def test_visit_if_f(self):
        if self.logging: print("testing: IfNodef")
        self.assertEqual(process_code("if false then 1 else 2 endif", self.baseEnv).get(), 2)

    def test_visit_if_t(self):
        if self.logging: print("testing: IfNodet")
        self.assertEqual(process_code("if true then 1 else 2 endif", self.baseEnv).get(), 1)

    def test_visit_if_tc(self):
        if self.logging: print("testing: IfNodetc")
        v = process_code("if 1 then 1 else 2 endif", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_insert(self):
        if self.logging: print("testing: Insert")
        self.assertEqual(str(process_code("insert->(1,[2,3])", self.baseEnv)), "[1, 2, 3]")

    def test_visit_insert_empty(self):
        if self.logging: print("testing: Insertn")
        self.assertEqual(str(process_code("insert->(1,[])", self.baseEnv)), "[1]")

    def test_visit_insert_tc(self):
        if self.logging: print("testing: Inserttc")
        v = process_code("insert->(1,3)", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_int(self):
        if self.logging: print("testing: IntegerNode")
        self.assertEqual(process_code("1", self.baseEnv).get(), 1)

    def test_visit_length(self):
        if self.logging: print("testing: Length")
        self.assertEqual(process_code("length->([1,2,3])", self.baseEnv).get(), 3)

    def test_visit_length_empty(self):
        if self.logging: print("testing: Lengthn")
        self.assertEqual(process_code("length->([])", self.baseEnv).get(), 0)

    def test_visit_length_tc(self):
        if self.logging: print("testing: Lengthtc")
        v = process_code("length->(3)", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_le(self):
        if self.logging: print("testing: LessEqualNode")
        self.assertEqual(process_code("2 <= 3", self.baseEnv).get(), True)

    def test_visit_le_f(self):
        if self.logging: print("testing: LessEqualNodef")
        self.assertEqual(process_code("2.0 <= 3.1", self.baseEnv).get(), True)

    def test_visit_lt(self):
        if self.logging: print("testing: LessNode")
        self.assertEqual(process_code("2 < 3", self.baseEnv).get(), True)

    def test_visit_lt_f(self):
        if self.logging: print("testing: LessNodef")
        self.assertEqual(process_code("2.0 < 3.1", self.baseEnv).get(), True)

    def test_visit_list_literal(self):
        if self.logging: print("testing: ListNode")
        self.assertEqual(str(process_code("[1,2,3]", self.baseEnv)), "[1, 2, 3]")

    def test_visit_list_fn(self):
        if self.logging: print("testing: ListNode1")
        self.assertEqual(str(process_code("list->(1,2,3)", self.baseEnv)), "[1, 2, 3]")

    def test_visit_list_single(self):
        if self.logging: print("testing: ListNode2")
        self.assertEqual(str(process_code("list->(3)", self.baseEnv)), "[3]")

    def test_visit_listp_true(self):
        if self.logging: print("testing: ListNodep")
        self.assertEqual(process_code("listp->([1,2,3])", self.baseEnv).get(), True)

    def test_visit_listp_true_empty(self):
        if self.logging: print("testing: ListNodepn")
        self.assertEqual(process_code("listp->([])", self.baseEnv).get(), True)

    def test_visit_listp_tc(self):
        if self.logging: print("testing: Listptc")
        self.assertEqual(process_code("listp->(3)", self.baseEnv).get(), False)

    def test_visit_list_nested(self):
        if self.logging: print("testing: ListNodem")
        self.assertEqual(str(process_code("[1,2,[3,4]]", self.baseEnv)), "[1, 2, [3, 4]]")

    def test_visit_mul(self):
        if self.logging: print("testing: MultiplyNode")
        self.assertEqual(process_code("2*3", self.baseEnv).get(), 6)

    def test_visit_mul_f(self):
        if self.logging: print("testing: MultiplyNodef")
        self.assertEqual(process_code("2.0*3.1", self.baseEnv).get(), 6.2)

    def test_visit_neq(self):
        if self.logging: print("testing: NotEqualNode")
        self.assertEqual(process_code("2 != 3", self.baseEnv).get(), True)

    def test_visit_neq_f(self):
        if self.logging: print("testing: NotEqualNodef")
        self.assertEqual(process_code("2.0 != 3.1", self.baseEnv).get(), True)

    def test_visit_not(self):
        if self.logging: print("testing: NotNode")
        self.assertEqual(process_code("!true", self.baseEnv).get(), False)

    def test_visit_null(self):
        if self.logging: print("testing: NullNode")
        self.assertEqual(str(process_code("[]", self.baseEnv)), "[]")

    def test_visit_numberp_int(self):
        if self.logging: print("testing: Numberp")
        self.assertEqual(process_code("numberp->(1)", self.baseEnv).get(), True)

    def test_visit_numberp_float(self):
        if self.logging: print("testing: Numberpf")
        self.assertEqual(process_code("numberp->(1.2)", self.baseEnv).get(), True)

    def test_visit_numberp_tc(self):
        if self.logging: print("testing: Numberptc")
        self.assertEqual(process_code("numberp->([1])", self.baseEnv).get(), False)

    def test_visit_or(self):
        if self.logging: print("testing: OrNode")
        self.assertEqual(process_code("true | false", self.baseEnv).get(), True)

    def test_visit_pairp(self):
        if self.logging: print("testing: Pairp")
        self.assertEqual(process_code("pairp->([1,2,3])", self.baseEnv).get(), True)

    def test_visit_pairp_empty(self):
        if self.logging: print("testing: Pairpf")
        self.assertEqual(process_code("pairp->([])", self.baseEnv).get(), False)

    def test_visit_pairp_tc(self):
        if self.logging: print("testing: Pairptc")
        v = process_code("pairp->(3)", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_rest(self):
        if self.logging: print("testing: Rest")
        self.assertEqual(str(process_code("rest->([1,2,3])", self.baseEnv)), "[2, 3]")

    def test_visit_restn(self):
        if self.logging: print("testing: Restn")
        v = process_code("rest->([])", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_rest_tc(self):
        if self.logging: print("testing: Resttc")
        v = process_code("rest->(3)", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_string(self):
        if self.logging: print("testing: StringNode")
        self.assertEqual(str(process_code("'Hi'", self.baseEnv)), "''Hi''")

    def test_visit_sub(self):
        if self.logging: print("testing: SubNode")
        self.assertEqual(process_code("2-3", self.baseEnv).get(), -1)

    def test_visit_sub_f(self):
        if self.logging: print("testing: SubNodef")
        self.assertAlmostEqual(process_code("2.0-3.1", self.baseEnv).get(), -1.1, places=6)

    def test_visit_switch_f(self):
        if self.logging: print("testing: SwitchNodef")
        self.assertEqual(process_code("switch {    case false: 1    case true:  2    default: 3 }", self.baseEnv).get(), 2)

    def test_visit_switch_t(self):
        if self.logging: print("testing: SwitchNodet")
        self.assertEqual(process_code("switch {   case true: 1   case true:  2    default: 3 }", self.baseEnv).get(), 1)

    def test_visit_switch_d(self):
        if self.logging: print("testing: SwitchNodeNoded")
        self.assertEqual(process_code("switch {   case false: 1   case false:  2    default: 3 }", self.baseEnv).get(), 3)

    def test_visit_switch_tc(self):
        if self.logging: print("testing: Switchtc")
        v = process_code("switch {  case false: 1  case 4:  2  default: 3 }", self.baseEnv)
        self.assertIsInstance(v, ErrorValue)

    def test_visit_true(self):
        if self.logging: print("testing: True")
        self.assertEqual(process_code("true", self.baseEnv).get(), True)

if __name__ == "__main__":
    unittest.main()
