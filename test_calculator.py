"""
Unit tests for calculator
"""

import calculator


class TestCalculator:
    def test_add(self):
        assert 3 == calculator.add(1, 2)

    def test_subtract(self):
        assert 2 == calculator.sub(3, 1)

    def test_multiply(self):
        assert 100 == calculator.multiply(10, 10)

    def test_divide(self):
        assert 10 == calculator.divide(100, 10)
