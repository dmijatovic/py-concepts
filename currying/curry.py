# Currying
# Log function that takes system name
# and returns log function to use later
def logFn(system):
  def msg(message):
    print("%s: %s" %(system, message))
  return msg


printerLog = logFn("printer")
printerLog("This is my printer log message")
mouseLog = logFn("mouse")
mouseLog("This is my first mouse message")

printerLog("And how the printer is telling me something")
mouseLog("Wait the mouse is also in trouble?!?")
