
def divide(top,bottom):
  # print("divide",top,bottom)
  return top/bottom

def multiply(first,second=100):
  # print("multiply",first,second)
  return first * second

def makePctStr(value):
  return str(value)+"%"

def roundVal(value, dec=2):
  return round(value,dec)

def compose(*functions):
  fn = list(functions)
  def params(x,y):
    f = fn.pop(0)
    reduce = f(x,y)
    for f in fn:
      reduce = f(reduce)
    return reduce
  return params

def percentage(x,y):
  p = compose(divide, multiply, roundVal, makePctStr)
  return p(x,y)
