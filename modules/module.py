
moduleVariable="This is module variable"

def findIndex(dataArray=[], searchString=""):
  if searchString in dataArray:
    return "found"
  else:
    return "not found"