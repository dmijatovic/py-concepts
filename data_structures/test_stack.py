from data_structures.caller import Caller
from data_structures.stack import CallStack


def test_create_stack():
  q = CallStack()
  assert isinstance(q, CallStack)
  assert len(q) == 0


def test_create_queue_with_caller():
  caller = Caller("Dusan", "123456")
  q = CallStack(caller)
  assert len(q) == 1


def test_call_queue_pop_1():
  caller = Caller("Dusan", "123456")
  q = CallStack(caller)
  c = q.pop()
  assert c.phone == "123456"
  assert len(q) == 0


def test_call_queue_pop_3():
  caller = Caller("Dusan", "123456")
  q = CallStack(caller)
  q.push("Drako", "000000")
  q.push("Dirkje", "999999")
  c = q.pop()
  assert c.phone == "999999"
  assert len(q) == 2


def test_phone_list():
  caller = Caller("Dusan", "123456")
  q = CallStack(caller)
  q.push("Drako", "000000")
  q.push("Dirkje", "999999")
  lst = q.getPhoneList()
  # lst = q.getPhoneList()
  assert lst == ['999999', '000000', '123456']
