import pytest
import calc

class TestCalc:
  def test_add(self):
    x = calc.add(1,2)
    assert x == 3

  def test_div(self):
    assert calc.div(10,5)==2

  def test_mul(self):
    assert calc.mul(2,2)==4

  def test_pow(self):
    assert calc.pow(2,3)==8
