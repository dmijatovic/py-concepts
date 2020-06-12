from data_structures.caller import Caller


class CallQueue:
  def __init__(self, caller=None):
    self.__queue = []
    if caller:
      self.__queue.append(caller)

  def push(self, name, phone):
    caller = Caller(name, phone)
    self.__queue.append(caller)

  def pop(self):
    caller = self.__queue.pop(0)
    return caller

  def getPhoneList(self):
    phones = [x.phone for x in self.__queue]
    return phones

  def __len__(self):
    return len(self.__queue)
