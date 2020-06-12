from data_structures.queue import Caller, CallQueue


def test_create_queue():
  q = CallQueue()
  assert isinstance(q, CallQueue)
  assert len(q) == 0


def test_create_queue_with_caller():
  caller = Caller("Dusan", "123456")
  q = CallQueue(caller)
  assert len(q) == 1


def test_call_queue_pop_1():
  caller = Caller("Dusan", "123456")
  q = CallQueue(caller)
  c = q.pop()
  assert c.phone == "123456"
  assert len(q) == 0


def test_call_queue_pop_3():
  caller = Caller("Dusan", "123456")
  q = CallQueue(caller)
  q.push("Drako", "000000")
  q.push("Dirkje", "999999")
  c = q.pop()
  assert c.phone == "123456"
  assert len(q) == 2


def test_phone_list():
  caller = Caller("Dusan", "123456")
  q = CallQueue(caller)
  q.push("Drako", "000000")
  q.push("Dirkje", "999999")
  lst = q.getPhoneList()
  assert lst == ['123456', '000000', '999999']
