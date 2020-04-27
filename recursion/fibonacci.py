
def fib(num):
  # base case
  if num==0 or num==1:
    return num
  else:
    #recurring portion
    return fib(num-1) + fib(num-2)

y = 23
x = fib(y)

print("fibonacci(", str(y),")=", str(x))
