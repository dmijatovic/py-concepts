
from data_structures.linked_list import LinkedList, Node


def test_create_ll_node():
  node = Node('0001', {"data": "I am node 1"})
  assert node.id == '0001'


def test_create_ll_without_node():
  ll = LinkedList()
  assert isinstance(ll, LinkedList)
  assert ll.head == None


def test_create_ll_with_node():
  node = Node('0001', "String data")
  ll = LinkedList(node)
  assert ll.head == node


def test_add_node_to_list():
  node = Node('0001', "String data")
  ll = LinkedList(node)
  ll.addToList('0002', "String data")
  assert ll.head.id == '0002'
  assert ll.head.getNext() == node


def test_find_node_by_id():
  node = Node('0001', "String data")
  ll = LinkedList(node)
  ll.addToList('0002', "String data")
  ll.addToList('0003', "String data")
  ll.addToList('0004', "String data")

  n = ll.findById("0003")
  assert n.id == '0003'


def test_remove_node_by_id():
  node = Node('0001', "String data")
  ll = LinkedList(node)
  ll.addToList('0002', "String data")
  ll.addToList('0003', "String data")
  ll.addToList('0004', "String data")

  n = ll.removeNodeById("0004")
  assert n == True
  assert ll.head.id == "0003"
  n = ll.removeNodeById("0005")
  assert n == False
