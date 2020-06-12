
class Node:
  def __init__(self, id, data):
    pass
    # self.__previousNode = None
    self.id = id
    self.data = data
    self.__nextNode = None

  def setNext(self, node):
    if isinstance(node, Node) or node is None:
      self.__nextNode = node
    else:
      raise TypeError("The node must be of type Node or None")

  def getNext(self):
    return self.__nextNode

  def __repr__(self):
    if self.__nextNode == None:
      return f"Node {self.id} as LAST node"
    else:
      return f"Node {self.id} with nextNode {self.__nextNode.id}"


class LinkedList:
  def __init__(self, node=None):
    self.head = node

  def getHead(self):
    return self.head

  def addToList(self, id, data):
    new_node = Node(id, data)
    if self.head == None:
      self.head = new_node
    else:
      new_node.setNext(self.head)
      self.head = new_node

  def findById(self, id):
    if self.head == None:
      raise ValueError("Head node missing. Nothing to remove")

    node = self.head

    while node != None:
      if node.id == id:
        break
      else:
        node = node.getNext()

    return node

  def removeNodeById(self, id):
    if self.head == None:
      raise ValueError("Head node missing. Nothing to remove")

    node = self.head
    prevNode = None
    removed = False

    while node != None:
      if node.id == id:
        nextNode = node.getNext()
        if prevNode:
          prevNode.setNext(nextNode)
          removed = True
        elif node.id == self.head.id:
          self.head = nextNode
          removed = True
        else:
          self.head.setNext(nextNode)
          removed = True
        break
      else:
        prevNode = node
        node = node.getNext()

    return removed
