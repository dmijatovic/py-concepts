"""
In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

Fn = F(n-1) + F(n-2)

The beginning of the sequence is thus:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
"""
def fib(num):
  # base case
  if num==0 or num==1:
    return num
  else:
    #recurring portion
    return fib(num-1) + fib(num-2)

y = 7
x = fib(y)

print("fibonacci(", str(y),")=", str(x))
