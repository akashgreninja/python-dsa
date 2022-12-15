

class Heap:
    def __init__(self, size):
        self.size = size+1
        self.customList = (size+1)*[None]
        self.size = 0


def peek(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]


def size(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.size


def levelordertransvarsal(rootnode):
    if not rootnode:
        return
    else:
        for i in range(1, rootnode.size+1):
            print(rootnode.customList[i])


def heapifytreeinsert(rootnode, index, heapType):
    # we divide it by 2 as the formula to find the left parent node was 2x
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootnode.customList[index] < rootnode.customList[parentIndex]:
            # temp=rootnode.customList[parentIndex]
            # rootnode.customList[parentIndex]=rootnode.customList[index]
            # rootnode.customList[index] =temp
            temp = rootnode.customList[index]
            rootnode.customList[index] = rootnode.customList[parentIndex]
            rootnode.customList[parentIndex] = temp

        heapifytreeinsert(rootnode, parentIndex, heapType)

    elif heapType == "Max":
        if rootnode.customList[index] > rootnode.customList[parentIndex]:
            temp = rootnode.customList[index]
            rootnode.customList[index] = rootnode.customList[parentIndex]
            rootnode.customList[parentIndex] = temp

        heapifytreeinsert(rootnode, parentIndex, heapType)


def insertNode(rootnode, nodevalue, heaptype):
    if rootnode.size+1 == rootnode.size:
        return "it is full"
    rootnode.customList[rootnode.size+1] = nodevalue
    rootnode.size += 1
    heapifytreeinsert(rootnode, rootnode.size, heaptype)
    return "inserted the loop"



def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.size < leftIndex:
        return
    elif rootNode.size == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return

    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType):
    if rootNode.size == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.size]
        rootNode.customList[rootNode.size] = None
        rootNode.size -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode


newBinaryHeap = Heap(5)
insertNode(newBinaryHeap, 3, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
print(extractNode(newBinaryHeap,"Max"))
levelordertransvarsal(newBinaryHeap)
