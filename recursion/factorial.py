
def factorial(num):
  # base case
  if num == 1:
    return 1
  # recurring sequence
  else:
    return num * factorial(num-1)

x = factorial(10)

print("factorial(", str(10),")=", str(x))
