from data_structures.binary_tree import BinNode, BinTree


def test_create_empty_bin_tree():
  bt = BinTree()
  assert isinstance(bt, BinTree)
  assert len(bt) == 0


def test_create_bin_tree_with_node():
  node = BinNode(1)
  bt = BinTree(node)
  assert len(bt) == 1
  bt.add(2)
  assert len(bt) == 2
  assert bt.head.rightNode.value == 2
  assert bt.head.leftNode == None


def test_add_head_node():
  bt = BinTree()
  a = bt.add(1)
  assert a == True
  assert bt.head.value == 1


def test_add_right_node():
  bt = BinTree()
  a = bt.add(1)
  assert a == True
  assert bt.head.value == 1
  a = bt.add(3)
  assert a == True
  assert bt.head.rightNode.value == 3


def test_add_left_node():
  bt = BinTree()
  a = bt.add(2)
  a = bt.add(1)
  assert a == True
  assert bt.head.leftNode.value == 1


def test_add_left_and_right_node():
  bt = BinTree()
  a = bt.add(2)
  a = bt.add(1)
  a = bt.add(3)
  a = bt.add(5)
  assert a == True
  assert len(bt) == 4
  # assert bt.head == "1-2-3"
