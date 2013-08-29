#! /usr/bin/env python

import sys
import util
import datetime

input_file = open(sys.argv[1], 'r')
base = int(input_file.readline()) # Get the base weight
line = input_file.readline()
edges = [] # Store the edges from the input file in a list
distance = 0 # The distance the bird needs to travel
print "Begin Parsing Input File"
while line:
  nums = line.split() # [start, end, weight]
  num1 = int(nums[1])
  distance = max(num1, distance) # Keep track of the maximum travel distance
  edges.append((int(nums[0]), num1, int(nums[2])))
  line = input_file.readline()
input_file.close()
print "Finished Parsing Input File"
print "Constructing Graph"
graph = []
for i in range(0, distance + 1):
  graph.append(util.Vertex(i))
for edge in edges:
  graph[edge[0]].add_edge(util.Edge(graph[edge[0]], graph[edge[1]], edge[2], original=True))
print "Finished Constructing Graph"

print "Finding the Optimal Sequence of Jetstreams"
solution = []
expanded = set()
frontier = util.PriorityQueue()
start = graph[0] # Start at node 0
expanded.add(start)
successors = start.get_edges()
if len(successors) == 0:
  frontier.push([util.Edge(graph[0], graph[1], base)], base)
else:
  for successor in successors:
    frontier.push([successor], successor.weight)
while not frontier.isEmpty():
  priority, l = frontier.pop()
  node = l[-1]
  if node.end == graph[distance]:
    for item in l:
      if item.original:
        solution.append((item.start.name, item.end.name))
    print solution
    print "Minimum Total Energy: " + str(priority)
    break
  elif graph[node.end.name] in expanded:
    print len(frontier)
    continue
  else:
    expanded.add(graph[node.start.name])
    successors = node.end.get_edges()
    if not node.original:
      l.pop()
    if len(successors) == 0:
      if graph[node.end.name + 1] not in expanded:
        successor = util.Edge(graph[node.end.name], graph[node.end.name + 1], base)
        new_priority = priority + successor.weight
        l.append(successor)
        frontier.push(l, new_priority)
    elif len(successors) == 1:
      if graph[successors[0].end.name] not in expanded:
        successor = successors[0]
        new_priority = priority + successor.weight
        l.append(successor)
        frontier.push(l, new_priority)
    else:
      for successor in successors:
        if graph[successor.end.name] not in expanded:
          copy = l[:]
          new_priority = priority + successor.weight
          copy.append(successor)
          frontier.push(copy, new_priority)
