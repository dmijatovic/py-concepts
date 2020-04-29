import time

"""
Queue manager returns one item from the list when next is called
"""
def queueManager(lst=[]):
  for item in lst:
    yield item

"""
The processing module does lot of work
"""
def processingModule(fileName):
  print("Processing lot of work with...", fileName)
  time.sleep(3)
  return "DONE"

# calling generator
fileList = ['file 1', 'file 2', 'file 3']
queue = queueManager(fileList)

loop=True
while loop:
  try:
    fileName = next(queue)
    stat = processingModule(fileName)
    print(fileName, stat)
  except StopIteration:
    loop = False

print("Done this HUGE task per item")