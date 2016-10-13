#!/bin/usr/env python

import collections

#################################
## Python implementation for
## Breath First Search
## Reference : http://www.redblobgames.com/pathfinding/a-star/implementation.html

DIAGRAM_WALLS1 = [(21, 0),(21, 1), (21, 2),(21, 3),(21, 4),(21, 5),
        (22, 0),(22, 1),(22, 2),(22, 3),(22, 4),(22, 5),
        (23, 0),(23, 1),(23, 2),(23, 3),(23, 4),(23, 5),
        (24, 4),(24, 4),(25, 4),(26, 4),(26, 5),
        (24, 5),(24, 5),(25, 5),(26, 5),
        (4, 10), (4, 11), (4, 12), (4,13), (4, 14),
        (5, 10), (5, 11), (5, 12), (5,13), (5, 14)]

class SimpleGraph:
    def __init__(self):
        self.edges = {}
    def neighbors(self, id):
        return self.edges[id]

class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wall = []
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    def passable(self, id):
        return id not in self.walls
    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0:
            results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    def empty(self):
        return len(self.elements) == 0
    def put(self, x):
        self.elements.append(x)
    def get(self):
        return self.elements.popleft()

#################################
## The representation of the Graph
## will be
##      (E)
##
## (B)        (D)
##
##   (C)   (A)
## With:
##  (A) -> (B)
##  (B) -> (A), (C), (D)
##  (C) -> (A)
##  (D) -> (E) (A)
##  (E) -> (B)
##
def InitGraph():
    ex_graph = SimpleGraph()
    ex_graph.edges = {
            'A': ['B'],
            'B': ['A', 'C', 'D'],
            'C': ['A'],
            'D': ['E', 'A'],
            'E': ['B']
            }
    return ex_graph

def InitGrid():
    ex_grid = SquareGrid(30, 15)
    ex_grid.walls = DIAGRAM_WALLS1
    DrawGrid(ex_grid)
    return ex_grid

def DrawGrid(grid):
    string = ''
    for y in range(0, grid.height):
        for x in range(0, grid.width):
            if grid.passable((x, y)):
                string += '.'
            else:
                string += '#'
        string += '\n'
    print(string)

def DrawGrid2(templategrid, grid2):
    # To do implement the draw
    pass

def BreathFirstSearch(graph, start):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        print("Visiting {}".format(current))
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

def BreathFirstSearch2(graph, start):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        print("Visiting {}".format(current))
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = None
        return came_from



if __name__ == "__main__":
    BreathFirstSearch(InitGraph(), 'A')
    parent = BreathFirstSearch2(InitGrid(), (8, 7))

