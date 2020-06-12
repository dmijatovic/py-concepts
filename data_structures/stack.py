from data_structures.caller import Caller


class CallStack:
  def __init__(self, caller=None):
    self.__queue = []
    if caller:
      self.__queue.append(caller)

  def push(self, name, phone):
    caller = Caller(name, phone)
    self.__queue.append(caller)

  def pop(self):
    caller = self.__queue.pop()
    return caller

  def getPhoneList(self):
    # copy queue
    stack = list(self.__queue)
    # reverse order
    stack.reverse()
    # extract phones
    phones = [x.phone for x in stack]
    return phones

  def __len__(self):
    return len(self.__queue)
