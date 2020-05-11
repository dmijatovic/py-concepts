import pytest
import chain

class TestChain:
  # needs to start with test_
  def test_divide(self):
    res = chain.divide(1,10)
    assert res == 1/10

  def test_multiply(self):
    res = chain.multiply(2,10)
    assert res==20

  def test_multiply_optional(self):
    res = chain.multiply(2)
    assert res==200

# call testmodule main to start
# if __name__=='__main__':
#   pytest.main()

