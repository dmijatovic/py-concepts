
from graph import Graph

def test1():
  myG = Graph()
  myG.addNode("A")
  myG.addNode("B")
  myG.addNode("C")

  myG.addEdge("A","C")
  myG.addEdge("A","B")
  myG.addEdge("B","C")

  # myG.removeEdge("A","B")
  myG.removeNode("A")

  print(myG)

def createGraph():
  myG = Graph()

  myG.addNode("A")
  myG.addNode("B")
  myG.addNode("C")
  myG.addNode("D")
  myG.addNode("E")
  myG.addNode("F")

  myG.addEdge("A","B")
  myG.addEdge("A","C")
  myG.addEdge("B","D")
  myG.addEdge("C","E")
  myG.addEdge("D","E")
  myG.addEdge("D","F")
  myG.addEdge("E","F")

  return myG

G = createGraph()
pathFrom = G.BFS("A")

print(G)
print(pathFrom)