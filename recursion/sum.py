
def sumElements(lst):
  if len(lst)==1:
    return lst[0]
  else:
    return lst[0] + sumElements(lst[1:])

y=[10,10,5,5,5]
x = sumElements(y)

print("Sum elements: ", str(x))
