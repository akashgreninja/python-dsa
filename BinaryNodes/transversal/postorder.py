import QueueList as queue
class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None
    

tree=BinaryTree("Drinks")
leftchild=BinaryTree("Hot")
rightchild=BinaryTree("Cold")
tree.leftnode=leftchild # type: ignore
tree.rightnode=rightchild  # type: ignore



def postOrderTraversal(root):
    if not root:
        return
    postOrderTraversal(root.leftnode)
    postOrderTraversal(root.rightnode)
    print(root.data)

def levelOrderTraversal(root):
    if not root:
        return
    
    customqueue=queue.Queue()
    customqueue.enqueue(tree)
    while not(customqueue.isEmpty()):
        root=customqueue.Enqueue()
        print(root.value.data)
   
        if(root.value.leftnode is not None):# type: ignore
            customqueue.enqueue(root.value.leftnode)# type: ignore
        if(root.value.rightnode is not None):# type: ignore
            customqueue.enqueue(root.value.rightnode)# type: ignore
    
   

# levelOrderTraversal(tree)
def search(root,rootvalue):
    # now first we put the binary tree in a queue and get the last value using deque and comapre its value if the last node has a right or left value we enqueue it and check again first in first out method
        if not root:
            return
        customqueue=queue.Queue()
        customqueue.enqueue(tree)
        while not (customqueue.isEmpty()):
            root=customqueue.Enqueue()
            if root.value.data==rootvalue:
                return "sucess"
            if(root.value.leftnode is not None):
                customqueue.enqueue(root.value.leftnode)
            if(root.value.rightnode is not None):
                customqueue.enqueue(root.value.rightnode)
        return "nothinh"

# print(search(tree,"Hot"))
# postOrderTraversal(tree)

def insertNodeBT(rootNode,Newnode):
    if not  rootNode:
        return
    customqueue=queue.Queue()
    customqueue.enqueue(rootNode)
    while not  (customqueue.isEmpty()):
        root=customqueue.Enqueue()
        if root.value.leftnode is not None:
            customqueue.enqueue(root.value.leftnode)
        else:
            root.value.leftnode=Newnode
            return"sucess"
        if root.value.rightnode is not None:
            customqueue.enqueue(root.value.rightnode)
        else:
            root.value.rightnode=Newnode
            return"sucess"



# newnode=BinaryTree("juice")
# print(insertNodeBT(tree,newnode))
# levelOrderTraversal(tree)
        

def DeepestNode(node):
    if not node:
        return
    customqueue=queue.Queue()
    customqueue.enqueue(node)
    while not (customqueue.isEmpty()):
        root=customqueue.Enqueue()
        if(root.value.leftnode is not None):
            customqueue.enqueue(root.value.leftnode)
        if(root.value.rightnode is not None):
            customqueue.enqueue(root.value.rightnode)
    deepestnode=root.value
    return deepestnode

# deepnode=DeepestNode(tree)
# print(deepnode.data)


def deleteDeepestNode(rootNode,dnode):
    if not rootNode:
        return
    customqueue=queue.Queue()
    customqueue.enqueue(rootNode)
    while not (customqueue.isEmpty()):
        root=customqueue.Enqueue()
        if root.value==dnode:
            root.value=None
            return
        
        if root.value.rightnode:
            if root.value.rightnode==dnode:
                root.value.rightnode=None
                return 
            else:
                customqueue.enqueue(root.value.rightchild)
        
        if root.value.leftnode:
            if root.value.leftnode==dnode:
                root.value.leftnode=None
                return 
            else:
                customqueue.enqueue(root.value.leftchild)


# newnode=DeepestNode(tree)
# deleteDeepestNode(tree,newnode)
# levelOrderTraversal(tree)

def finaldelete(value,tree):
    if  not tree :
        return
    customqueue=queue.Queue()
    customqueue.enqueue(tree)
    while not (customqueue.isEmpty()):
        root=customqueue.Enqueue()
        if root.value.data==value:
            locate=DeepestNode(tree)
      
            root.value.data=locate.data
            deleteDeepestNode(tree,locate)
            return "node has been deleted"


        if(root.value.leftnode is not None):# type: ignore
            customqueue.enqueue(root.value.leftnode)# type: ignore
        if(root.value.rightnode is not None):# type: ignore
            customqueue.enqueue(root.value.rightnode)# type: ignore
    return"failed"

print(finaldelete("Drinks",tree))
levelOrderTraversal(tree)


    


