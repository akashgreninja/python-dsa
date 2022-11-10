from LinkedList import SingleLinkedList


def partition(check,x):
    curnode=check.head
    check.tail=check.head

    while curnode:
        nextnode=curnode.next
        curnode.next=None
        if curnode.value< x:
            curnode.next=check.head
            # print(check.head)
            check.head=curnode
        
        else:
            check.tail.next=curnode
            check.tail=curnode
        curnode=nextnode
    
    if check.tail.next is not None:
        check.tail.tail=None



LinkedList=SingleLinkedList()
LinkedList.randomvar(10,0,99)
print(LinkedList)

partition(LinkedList,30)
print(LinkedList)
