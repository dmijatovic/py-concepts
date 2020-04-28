import unittest
import chain


class TestChain(unittest.TestCase):
  # needs to start with test_
  def test_divide(self):
    res = chain.divide(1,10)
    self.assertEqual(res,1/10)

  def test_multiply(self):
    res = chain.multiply(2,10)
    self.assertEqual(res,20)

  def test_multiply_optional(self):
    res = chain.multiply(2)
    self.assertEqual(res,100)

# call testmodule main to start
if __name__=='__main__':
  unittest.main()

