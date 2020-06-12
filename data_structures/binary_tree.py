

class BinNode:
  def __init__(self, value):
    self.value = value
    self.leftNode = None
    self.rightNode = None

  def __repr__(self):
    return f"[{self.leftNode}-{self.value}-{self.rightNode}]"


class BinTree:
  def __init__(self, node=None):
    self.__len = 0
    if node:
      self.head = node
      self.__increment()
    else:
      self.head = None

  def __increment(self):
    self.__len += 1

  def __decrement(self):
    if self.__len > 0:
      self.__len -= 1

  def add(self, value):
    new_node = BinNode(value)
    if self.head == None:
      self.head = new_node
      self.__increment()
      return True

    node = self.head

    while node != None:
      if node.value > value:
        if node.leftNode == None:
          node.leftNode = new_node
          self.__increment()
          return True
        else:
          node = node.leftNode
      elif node.value < value:
        if node.rightNode == None:
          node.rightNode = new_node
          self.__increment()
          return True
        else:
          node = node.rightNode
      else:
        raise KeyError("The node with this value already exists")

    return False

  def find(self, value):
    pass

  def __len__(self):
    return self.__len
