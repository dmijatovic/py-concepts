"""
Create recursive functio to traverse dictionary and look for specific value.
The function should return a list of keys where the value is found.
"""
tree={
  '1':{
    '1.1':{
      '1.1.1':"Find me"
    },
    '1.2':"Nothing here"
  },
  '2':'Find me',
  '3':{
    '3.1':['Not here','Not here', 'Find me'],
    '3.2':{
      '3.2.1':'Not here',
      '3.2.2':{
        '3.2.2.1':"Find me"
      }
    },
    '3.3':[{
      '3.3.1':"Not here"
    },{
      '3.3.2':"Not here"
    },{
      '3.3.3':"Find me"
    }]
  }
}


def appendResult(total, key, value):
  if isinstance(value, list):
    total.extend(value)
  elif isinstance(value, bool):
    if value==True: total.append(key)
  elif isinstance(value, str):
    total.append(value)
  else:
    print("What to do with...", value)
  return total


def findValInDictionary(value, collection, parentKey=None):
  found=[]
  # base case
  if isinstance(collection, str):
    if collection == value:
      return True
    else:
      return False
  # recurring instance calling itself
  elif isinstance(collection, list):
    for index in collection:
      val = findValInDictionary(value, index, parentKey)
      found = appendResult(found,parentKey,val)
  # recurring instance calling itself
  else:
    for key in collection:
      val = findValInDictionary(value, collection[key], key)
      found = appendResult(found,key,val)
    # print("Not supported type...", type(dict[key]))
# always return found list
  return found

positions = findValInDictionary("Find me", tree)

print("Find me at keys: ", positions)