class GraphNode:
    def __init__(self, vertex=0, next_node=None):
        self.vertex = vertex
        self.next = next_node

class Graph:
    MAX = 8

    def __init__(self):
        self.headnodes = [None] * self.MAX
        self.n = 0
        self.visited = [False] * self.MAX

    def initialize_visited(self):
        self.visited = [False] * self.MAX

    def vertexExists(self, vertex):
        return self.headnodes[vertex] is not None

    def addVertex(self, vertex):
        if self.headnodes[vertex] is None:
            self.headnodes[vertex] = GraphNode(vertex)
            self.n += 1

    def addEdge(self, vertex1, vertex2):
        if self.headnodes[vertex1] is not None and self.headnodes[vertex2] is not None:
            newNode = GraphNode(vertex2, self.headnodes[vertex1].next)
            self.headnodes[vertex1].next = newNode

    def printGraph(self):
        for i in range(self.MAX):
            if self.headnodes[i] is not None:
                print(f"{i} {cities[i]}:", end=" ")
                curr = self.headnodes[i].next
                neighbors = []
                while curr is not None:
                    neighbors.append(str(curr.vertex))
                    curr = curr.next
                print(", ".join(neighbors))
            else:
                print(f"Vertex {i}: x")


    def bfs(self, start, destination):
        if not self.vertexExists(start):
            print("Starting city doesn't exist!")
            return

        queue = []
        queue.append(start)
        self.visited[start] = True

        predecessor = [-1] * self.MAX

        while queue:
            current_vertex = queue.pop(0)

            if current_vertex == destination:
                path = []
                while current_vertex != -1:
                    path.append(current_vertex)
                    current_vertex = predecessor[current_vertex]
                path.reverse()
                print(" -> ".join(cities[vertex] for vertex in path))
                return

            current = self.headnodes[current_vertex]
            while current:
                if not self.visited[current.vertex]:
                    queue.append(current.vertex)
                    self.visited[current.vertex] = True
                    predecessor[current.vertex] = current_vertex
                current = current.next

        print("No path exists between the given cities.")

g = Graph()


cities = ["Lahore", "Kasur", "Jazira", "Bhakar", "Okara", "Jhang", "Khosab", "Sahiwal"]
d1 = {city: i for i, city in enumerate(cities)}


for i in range(8):
    g.addVertex(i)


g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 7)
g.addEdge(4, 1)
g.addEdge(4, 3)
g.addEdge(4, 6)
g.addEdge(5, 0)
g.addEdge(5, 3)
g.addEdge(6, 4)
g.addEdge(7, 5)


g.printGraph()


city1 = input("Enter name of starting city: ")
while city1 not in d1:
    print(f"{city1} is not a valid city, please re-enter.")
    city1 = input("Enter name of starting city: ")

city2 = input("Enter name of destination city: ")
while city2 not in d1:
    print(f"{city2} is not a valid city, please re-enter.")
    city2 = input("Enter name of destination city: ")

g.initialize_visited()
g.bfs(d1[city1], d1[city2])
