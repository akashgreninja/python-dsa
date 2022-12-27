from collections import defaultdict

class Graph:
    def __init__(self,noofvertices):
        self.graph=defaultdict(list)
        self.noofvertices=noofvertices
    
    def addedge(self,edge,vertex):
        self.graph[vertex].append(edge)

    def topohelp(self,v,visited,stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topohelp(i,visited,stack)
        
        stack.insert(0,v)

    def topologicalSort(self    ):
        visited=[]
        stack=[]
        for k in list(self.graph):
            if k not in visited:
                self.topohelp(k,visited,stack)
        print(stack)


graph=Graph(8)
graph.addedge("A","C")
graph.addedge("C","E")
graph.addedge("E","H")
graph.addedge("E","F")
graph.addedge("F","G")
graph.addedge("B","D")
graph.addedge("B","C")
graph.addedge("D","F")
graph.topologicalSort()