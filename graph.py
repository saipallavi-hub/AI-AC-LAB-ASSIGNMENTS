#Task-6 Graph Representation
#write a python code Use AI to implement a graph using an adjacency list.
#Sample Input Code:class Graph:pass
#Expected Output:Graph with methods to add vertices, add edges, and display connections.
class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def display(self):
        for v in self.graph:
            print(v, "->", self.graph[v])


g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")

g.add_edge("A", "B")
g.add_edge("A", "C")

g.display()