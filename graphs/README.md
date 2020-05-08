# Graph data structure

The graph data structure having nodes (vertex) and edges (connections).

## Types of graphs

- `Tree`: graph type that has number of nodes with only 1 path
- `Undirected graph`: there is no direction assotiated with edge (can go both directions)
- `Directed graph`: the edges have specific direction. The information can only travel in specific direction
- `Weighted graph`: the edges have specific value.

## Adjecency matrix

Data is stored in an 2 dimensional matrix. X and Y are nodes and value at crossection stores true/false connection between the nodes. Example

A1 A2 A3
A1 0 1 1
A2 1 0 0
A3 1 0 0

This is simular to correlation matrix but only has 0/1 value for true/false connection.

## Adjecency list

Stores the nodes connected (edges). Usually stored in array. Example

```python
graph={
  "A": ["B","F"],
  "B": ["A", "D"]
}
```

## Traversal

Visiting every single node. There are 2 approaches:

- DFS (depth-first-search): we follow the edges from start node untill we hit the end. In circulair graphs we need to keep track of nodes we already visited.
- BFS (breath-first-search): we first visit the all neigbors nodes, the we select one of these to proceed. Here we also need to keep track which nodes we already visited.
