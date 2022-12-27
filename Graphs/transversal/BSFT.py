class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def bsf(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            dequeue=queue.pop(0)
            print(dequeue)
            for x in self.gdict[dequeue]:
                if x not in visited:
                    visited.append(x)
                    queue.append(x)

    def dfs(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            popvertex=stack.pop()
            print(popvertex)
            for i in self.gdict[popvertex]:
                if i not in visited:
                    visited.append(i)
                    stack.append(i)



customDict={
    "a":["b","c"],
    "b":["a","d","e"],
    "c":["a","e"],
    "d":["b","e","f"],
    "e":["d","f"],
    "f":["d","e"]
}

graph=Graph(customDict)
# graph.bsf("a")
graph.dfs("a")