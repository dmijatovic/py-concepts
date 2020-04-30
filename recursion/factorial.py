"""
In mathematics, the factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example:
5! = 5 * 4 * 3 * 2 * 1 = 120
The value of 0! is 1, according to the convention for an empty product.
"""

def factorial(num):
  # base case
  if num == 1 or num == 0:
    return 1
  # recurring sequence
  else:
    return num * factorial(num-1)

x = factorial(10)

print("factorial(", str(10),")=", str(x))
