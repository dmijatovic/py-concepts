

# autopep8
# gt5_1 = lambda x: x>5
def gt5(x): return x > 5


# print(gt5(10))


def filterList(values, checkFn):
  return [val for val in values if checkFn(val)]


my_list = [1, 2, 3, 4, 5]
filtered_list = filterList(my_list, lambda x: x < 5)

# print(filtered_list)
new_list = list(filter(lambda x: x < 5, my_list))
# similair as filter
# print(new_list())


# def removeNumbers(value):

items = [
    {'code': 'usd', 'exchange_usd': 1.00},
    {'code': 'gbp', 'exchange_usd': 1.40},
    {'code': 'eur', 'exchange_usd': 1.20},
    {'code': 'jpy', 'exchange_usd': 0.30}
]

cur1 = list(map(lambda x: x['code'].upper(), items))

print("cur1...", cur1)

cur2 = list(map(lambda x: {x['code'].upper(), x['exchange_usd']}, items))

print("cur2...", cur2)
