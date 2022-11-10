


class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None
    

tree=BinaryTree("Drinks")
leftchild=BinaryTree("Hot")
rightchild=BinaryTree("Cold")
tree.leftnode=leftchild
tree.rightnode=rightchild


def preOrderTransvesal(root):
    if not root:
        return 
    print(root.data)
    preOrderTransvesal(root.leftnode)
    preOrderTransvesal(root.rightnode)


preOrderTransvesal(tree)
