"""
Graph class implemented using adjecency list approach. The graph
stores nodes and edges in an dictionary. Each node is a key in
dictionary. Edges are stored in a list. Each node holds the connections it
has with other nodes.
"""
class Graph:
  def __init__(self):
    self.nodes={}

  def __repr__(self):
    return f"Graph with nodes...{self.nodes}"

  def addNode(self,name):
    self.nodes[name]=[]

  def addEdge(self,fromNode, toNode):
    self.nodes[fromNode].append(toNode)
    self.nodes[toNode].append(fromNode)

  def removeNode(self, name):
    rNode = self.nodes[name]

    for node in rNode:
      self.removeNodeFromList(node,name)

    del self.nodes[name]

  def removeEdge(self, fromNode, toNode):
    self.removeNodeFromList(fromNode,toNode)
    self.removeNodeFromList(toNode,fromNode)

  def removeNodeFromList(self, node, listItem):
    pos = self.nodes[node].index(listItem)
    newList = self.nodes[node][:pos]
    newList.extend(self.nodes[node][pos+1:])
    self.nodes[node] = newList

  def BFS(self,node):
    """
    Breath-First-Search traversing graph
    """
    visited={}
    path=[]
    def traverseFrom(node):
      # base case
      if node==None:
        return None
      if node in self.nodes:
        visited[node] = True
        path.append(node)
        for neighbour in self.nodes[node]:
          if neighbour in visited:
            msg = f'already been there {neighbour}'
            print(msg)
          else:
            return traverseFrom(neighbour)
      else:
        return None
    # start recursion
    traverseFrom(node)
    return path