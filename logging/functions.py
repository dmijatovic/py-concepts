import logging
import os

file = os.getcwd() + "/logging/functions.log"

print("Logging to...", file)

logging.basicConfig(filename=file,
  level=logging.INFO,
  format="%(asctime)s|%(name)s|%(levelname)s|%(message)s",
  datefmt="%Y-%m-%d %H:%M")

def divide(top,bottom):
  # print("divide",top,bottom)
  msg = f"divide {top} by {bottom}"
  logging.info(msg)
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