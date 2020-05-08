import sys

# add module dir
sys.path.append("/home/dusan/iis/demo/python/concepts/modules/level1-modules")

# import module1 as m 
from module1 import sayHello

sayHello("Dusan")

