import heapq

class PriorityQueue:

  def __init__(self):
    self.heap = []

  def push(self, item, priority):
    pair = (priority, item)
    heapq.heappush(self.heap, pair)

  def pop(self):
    (priority, item) = heapq.heappop(self.heap)
    return priority, item

  def isEmpty(self):
    return len(self.heap) == 0

  def __str__(self):
    return str(self.heap)

  def __repr__(self):
    return str(self)

  def __len__(self):
    return len(self.heap)

class Vertex:

  def __init__(self, name):
    self.name = name
    self.edges = []

  def add_edge(self, edge):
    self.edges.append(edge)

  def get_edges(self):
    return self.edges

  def num_edges(self):
    return len(self.edges)

  def __str__(self):
    return ("Vertex: " + str(self.name) + ", Edges:" + str(self.edges))

  def __repr__(self):
    return str(self)

class Edge:

  def __init__(self, node1, node2, weight, original=False):
    self.start = node1
    self.end = node2
    self.weight = weight
    self.original = original

  def __str__(self):
    return "Edge:(" + str(self.start.name) + ", " + str(self.end.name) + ", " + str(self.weight) + ", original: " + str(self.original) + ")"

  def __repr__(self):
    return str(self)


