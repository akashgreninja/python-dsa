

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


def Inorder(root):
    if not root:
        return
    else:
        Inorder(root.leftnode)
        print(root.data)
        Inorder(root.rightnode)

Inordertransversel=Inorder(tree)