
# class Graph:
#     def __init__(self,gdict=None):
#         if gdict is None:
#             gdict={}
#         self.gdict=gdict

#     def addEdge(self,vertex,edge):
#         self.gdict[vertex].append(edge)

# customDict={
#     "a":["b","c"],
#     "b":["a","d","e"],
#     "c":["a","e"],
#     "d":["b","e","f"],
#     "e":["d","f"],
#     "f":["d","e"]
# }

# graph=Graph(customDict)
# graph.addEdge("e","c")
# print(graph.gdict["d"])
class Graph:
    def __init__(self):
        self.adj_list={}
    
    def addvertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex,":",self.adj_list[vertex])

    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False
    def  removeEdge(self,vertex1,vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            # there is no link b/w the two vertex we cannot identify it so we have used try except
            try:

                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
                return True
            except ValueError:
                pass
    def  removeVertex(self,vertex):
        if vertex in self.adj_list.keys():
            for i in self.adj_list[vertex]:
                self.adj_list[i].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

        
           

custom=Graph()
custom.addvertex("A")
custom.addvertex("B")
custom.addvertex("C")
custom.addvertex("D")
custom.addEdge("A","B")
custom.addEdge("A","C")
custom.addEdge("B","C")
custom.print_graph()
# custom.removeEdge("A","D")
custom.removeVertex("A")
custom.print_graph()