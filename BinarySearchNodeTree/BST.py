import QueueList
class BSTNode:
    def __init__(self,data) :
        self.data=data
        self.leftnode=None
        self.rightnode=None


def insertNode(rootnode,nodevalue):
    if rootnode.data==None:
        rootnode.data=nodevalue
    elif nodevalue<=rootnode.data:

        if rootnode.leftnode is None:
            rootnode.leftnode=BSTNode(nodevalue) 
        else:
            insertNode( rootnode.leftnode,nodevalue)
        
    else:
        
        if rootnode.rightnode is None:
            rootnode.rightnode=BSTNode(nodevalue)
        else:
            insertNode( rootnode.rightnode,nodevalue)
            
    return "sucess"


def preOrderTransvarsal(rootnode):
    # nlr
    if not rootnode:
        return 

    print(rootnode.data)
    preOrderTransvarsal(rootnode.leftnode)
    preOrderTransvarsal(rootnode.rightnode)

def InorderOrderTransvarsal(rootnode):
    # lnr
    if not rootnode:
        return 

   
    preOrderTransvarsal(rootnode.leftnode)
    print(rootnode.data)
    preOrderTransvarsal(rootnode.rightnode)


def PostorderOrderTransvarsal(rootnode):
    # lrn
    if not rootnode:
        return 

   
    preOrderTransvarsal(rootnode.leftnode)
    print(rootnode.data)
    preOrderTransvarsal(rootnode.rightnode)

def levelorderOrderTransvarsal(rootnode):

    if not rootnode:
        return 
    else:
        check=QueueList.Queue()
        check.enqueue(rootnode)
        while not (check.isEmpty()):
            value=check.Enqueue()
            print(value.value.data)
            if value.value.leftnode is not None:
                check.enqueue(value.value.leftnode)
                
            if value.value.rightnode is not None:
                check.enqueue(value.value.rightnode)

def search(rootnode,desdata):

    if not rootnode:
        return 
    else:
        check=QueueList.Queue()
        check.enqueue(rootnode)
        while not (check.isEmpty()):
            value=check.Enqueue()
            if desdata==value.value.data:
                return"found it"
            if value.value.leftnode is not None:
                check.enqueue(value.value.leftnode)
                
            if value.value.rightnode is not None:
                check.enqueue(value.value.rightnode)

        
def minValue(bstnode):
    current=bstnode
    while(current.leftnode is not None):
        current=current.leftnode
    return current


def deleteNode(rootnode,nodevalue):
    if not  rootnode:
        return
    if nodevalue<= rootnode.data:
        rootnode.leftnode=deleteNode(rootnode.leftnode,nodevalue)
    elif nodevalue< rootnode.data:
        rootnode.leftnode=deleteNode(rootnode.rightnode,nodevalue)
    else:
        if rootnode.leftnode is None:
            temp=rootnode.rightnode
            rootnode=None
            return temp

        if rootnode.rightnode is None:
            temp=rootnode.leftnode
            rootnode=None
            return temp

        temp=minValue(rootnode.rightnode)
        rootnode.data=temp.data
        rootnode.rightnode=deleteNode(rootnode.rightnode,temp.data)


def deleteall(rootnode):
    rootnode.data=None
    rootnode.leftnode=None
    rootnode.rightnode=None
  
newbinary=BSTNode(None)
insertNode(newbinary,70)
insertNode(newbinary,50)
insertNode(newbinary,90)
insertNode(newbinary,30)
insertNode(newbinary,60)
insertNode(newbinary,80)
insertNode(newbinary,100)
insertNode(newbinary,20)
insertNode(newbinary,40)



# print(search(newbinary,900))
# deleteNode(newbinary,100)
levelorderOrderTransvarsal(newbinary)
# print(newbinary.data)
# print(newbinary.leftnode.leftnode.data)