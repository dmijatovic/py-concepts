# Lambda functions in python

Lambda fn is short/dense way of writing simple functions. There are usually applied over an array of data.

```python

# lambda fn
res = lambda x: x > 5
# same as lambda fn above
# written in def notation
def res(x):
  return x > 5

```

## Using lambda fn

When using lambda with filter and map builtin python function you need to covert filter/map object back to list.

```python
# list of items
items = [
    {'code': 'usd', 'exchange_usd': 1.00},
    {'code': 'gbp', 'exchange_usd': 1.40},
    {'code': 'eur', 'exchange_usd': 1.20},
    {'code': 'jpy', 'exchange_usd': 0.30}
]

# transformation
cur1 = list(map(lambda x: x['code'].upper(), items))

print("cur1...", cur1)

```
