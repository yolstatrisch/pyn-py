"""
This is the test file for pyn
"""
import unittest
import math
import pyn
from pyn import *


__version__ = 0.3


class TestVersionCompatibility(unittest.TestCase):
    def test_version(self):
        self.assertGreaterEqual(pyn.__version__, __version__, msg='pyn.py version is lower than the unittest')


@unittest.skipIf(pyn.__version__ < 0.1, 'Function not supported')
class TestIdentityFunction(unittest.TestCase):
    def test_add_by_zero(self):
        self.assertEqual(add_by_zero(0), 0)
        self.assertEqual(add_by_zero(1), 1)
        self.assertEqual(add_by_zero(54564.25), 54564.25)
        self.assertEqual(add_by_zero(-1), -1)
        self.assertEqual(add_by_zero(-2123341.2319494), -2123341.2319494)

    def test_multiply_by_one(self):
        self.assertEqual(add_by_zero(0), 0)
        self.assertEqual(add_by_zero(1), 1)
        self.assertEqual(add_by_zero(376381.98997), 376381.98997)
        self.assertEqual(add_by_zero(-1), -1)
        self.assertEqual(add_by_zero(-1231.79), -1231.79)


@unittest.skipIf(pyn.__version__ < 0.1, 'Function not supported')
class TestMultiplyIntByZero(unittest.TestCase):
    def test_multiplication_zero(self):
        self.assertEqual(multiply_int_by_zero(0), 0)

    def test_multiplication_positive(self):
        self.assertEqual(multiply_int_by_zero(1), 0)
        self.assertEqual(multiply_int_by_zero(654), 0)

    def test_multiplication_negative(self):
        self.assertEqual(multiply_int_by_zero(-1), 0)
        self.assertEqual(multiply_int_by_zero(-94196143), 0)


@unittest.skipIf(pyn.__version__ < 0.1, 'Function not supported')
class TestIterMultiplyIntByZero(unittest.TestCase):
    def test_iter_multiplication_zero(self):
        self.assertEqual(i_multiply_int_by_zero(0), 0)

    def test_multiplication_positive(self):
        self.assertEqual(i_multiply_int_by_zero(1), 0)
        self.assertEqual(i_multiply_int_by_zero(654), 0)

    def test_multiplication_negative(self):
        self.assertEqual(i_multiply_int_by_zero(-1), 0)
        self.assertEqual(i_multiply_int_by_zero(-94196143), 0)


@unittest.skipIf(pyn.__version__ < 0.2, 'Function not supported')
class TestBitWiseAddition(unittest.TestCase):
    def test_bitwise_add_no_carry(self):
        self.assertTupleEqual(bit_addition(False, False), (False, False))
        self.assertTupleEqual(bit_addition(False, True), (True, False))
        self.assertTupleEqual(bit_addition(True, False), (True, False))
        self.assertTupleEqual(bit_addition(True, True), (False, True))

    def test_bitwise_add_carry(self):
        self.assertTupleEqual(bit_addition(False, False, True), (True, False))
        self.assertTupleEqual(bit_addition(False, True, True), (False, True))
        self.assertTupleEqual(bit_addition(True, False, True), (False, True))
        self.assertTupleEqual(bit_addition(True, True, True), (True, True))


@unittest.skipIf(pyn.__version__ < 0.1, 'Function not supported')
class TestAbs(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(f_abs(0), math.fabs(0))

    def test_positive(self):
        self.assertEqual(f_abs(0.333333), math.fabs(0.333333))
        self.assertEqual(f_abs(1), math.fabs(1))
        self.assertEqual(f_abs(56415486.1), math.fabs(56415486.1))

    def test_negative(self):
        self.assertEqual(f_abs(-0.6465415), math.fabs(-0.6465415))
        self.assertEqual(f_abs(-1), math.fabs(-1))
        self.assertEqual(f_abs(-23356236.45646546), math.fabs(-23356236.45646546))


@unittest.skipIf(pyn.__version__ < 0.1, 'Function not supported')
class TestNegate(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(negate(0), 0)

    def test_positive(self):
        self.assertEqual(negate(1), -1)
        self.assertEqual(negate(2.54), -2.54)
        self.assertEqual(negate(2.012), -2.012)
        self.assertEqual(negate(2.757), -2.757)
        self.assertEqual(negate(5456412315465), -5456412315465)

    def test_negative(self):
        self.assertEqual(negate(-1), 1)
        self.assertEqual(negate(-2.54), 2.54)
        self.assertEqual(negate(-42.012), 42.012)
        self.assertEqual(negate(-245451231587445), 245451231587445)


@unittest.skipIf(pyn.__version__ < 0.2, 'Function not supported')
class TestFasterSign(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(faster_sign(0), 0)
        self.assertEqual(faster_sign(00), 0)

    def test_positive(self):
        self.assertEqual(faster_sign(1), 1)
        self.assertEqual(faster_sign(0.5), 1)
        self.assertEqual(faster_sign(5456412315465), 1)
        self.assertEqual(faster_sign(1564651313112.1341), 1)

    def test_negative(self):
        self.assertEqual(faster_sign(-1), -1)
        self.assertEqual(faster_sign(-0.31), -1)
        self.assertEqual(faster_sign(-245451231587445), -1)
        self.assertEqual(faster_sign(-911465488484684.1578), -1)


@unittest.skipIf(pyn.__version__ < 0.1, 'Function not supported')
class TestSign(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(sign(0), 0)
        self.assertEqual(sign(00), 0)

    def test_positive(self):
        self.assertEqual(sign(1), 1)
        self.assertEqual(sign(0.5), 1)
        self.assertEqual(sign(5456412315465), 1)
        self.assertEqual(sign(1564651313112.1341), 1)

    def test_negative(self):
        self.assertEqual(sign(-1), -1)
        self.assertEqual(sign(-0.31), -1)
        self.assertEqual(sign(-245451231587445), -1)
        self.assertEqual(sign(-911465488484684.1578), -1)


if __name__ == '__main__':
    unittest.main(verbosity=0)
