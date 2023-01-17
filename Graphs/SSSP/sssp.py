

class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict


    def bfs(self,start,end):
        queue=[]
        queue.append([start])
        while queue:
            la=queue.pop(0)
            node=la[-1]
            if node==end:
                return la
        
            for adj in self.gdict.get(node,[]):
                new_path=list(la)
                new_path.append(adj)
                queue.append(new_path)

customDict={
    "a":["b","c"],
    "b":["d","g"],
    "c":["d","e"],
    "d":["f"],
    "e":["f"],
    "g":["f"]
}

g=Graph(customDict)
print(g.bfs("a","e"))