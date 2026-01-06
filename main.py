#класс узла

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


#Adjacency List

class AdjacencyList:
    def __init__(self):
        self.edges = []

    def build(self, node):
        for child in node.children:
            self.edges.append((node.value, child.value))
            self.build(child)

    def print(self):
        for parent, child in self.edges:
            print(f"{parent} => {child}")


#Materialized Path

class MaterializedPath:
    def __init__(self):
        self.paths = []

    def build(self, node, parent_path=""):
        current_path = node.value if parent_path == "" else parent_path + "/" + node.value
        self.paths.append((node.value, current_path))

        for child in node.children:
            self.build(child, current_path)

    def print(self):
        for _, path in self.paths:
            print(path)


#создание дерева

start = Node("TRANSPORT")

b = Node("BOAT")
c = Node("CAR")
d = Node("AIRCRAFT")

e = Node("YACHT")
f = Node("SAILBOAT")

j = Node("SEDAN")
k = Node("VAN")
l = Node("TRACK")

g = Node("JET")
h = Node("AIRBUS")
i = Node("HELICOPTER")

start.add_child(b)
start.add_child(c)
start.add_child(d)

b.add_child(e)
b.add_child(f)

c.add_child(j)
c.add_child(k)
c.add_child(l)

d.add_child(g)
d.add_child(h)
d.add_child(i)


#запуск

print("Adjacency List:")
adj = AdjacencyList()
adj.build(start)
adj.print()

print("\nMaterialized Path:")
mp = MaterializedPath()
mp.build(start)
mp.print()

