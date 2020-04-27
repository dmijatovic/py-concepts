"""
This example shows simple function composition approach for
calculating percentages from 2 numbers. The basic operations
are divide and multiply. For multiply we set second argument
to default to 100. Doing this we have basic multiply function
we could use for multiplying two numbers and calculating
percentage in case the second argument is not provided.
"""

def divide(top,bottom):
  return top/bottom

def multiply(first,second=100):
  return first * second

def compose(fn1,fn2):
  def params(x,y):
    return fn2(fn1(x,y))
  return params

# d = divide(5,100)
# m = multiply(d,100)
# print(d,m)

percent = compose(divide, multiply)
val = percent(5,100)

print(val,"%")
