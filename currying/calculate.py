
def mathWith(n1):
  def add(n2):
    return n1 + n2
  def multiply(n2):
    return n1 * n2
  return add, multiply

addTo5, mulWith5 = mathWith(5)

# print(x5["add"](3))
# print(x5["multiply"](3))

print(addTo5(6))
print(mulWith5(6))