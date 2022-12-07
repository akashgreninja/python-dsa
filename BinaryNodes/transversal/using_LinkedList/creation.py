

class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children
    
    def __str__(self,level=0):
        ret=" "* level +str(self.data) +'\n'
        for child in self.children:
            ret+=child.__str__(level +1)
        return ret
    

    def addChild(self,TreeNode):
        self.children.append(TreeNode)


tree=TreeNode('drinks',[])
cold=TreeNode('cold',[])
hot=TreeNode('hot',[])
tree.addChild(cold)
tree.addChild(hot)
coffee=TreeNode('coffee',[])
tea=TreeNode('tea',[])
fanta=TreeNode('fanta',[])
coco=TreeNode('coco',[])
hot.addChild(coffee)
hot.addChild(tea)
cold.addChild(coco)
cold.addChild(fanta)
print(tree)

