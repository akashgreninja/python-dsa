
from LinkedList import SingleLinkedList



def removeDups(test):
    if test.head is None:
        return 
    
    else:
        curnode=test.head
        
        values=set([curnode.value])
        while curnode.next is not None:
            if curnode.next.value in values:    
                curnode.next=curnode.next.next
            else:
                values.add(curnode.next.value)
                curnode=curnode.next
        return test

def removedupwithout(test):
    if test.head==None:
        return
    
    else:
        tempnode=test.head

        
        while tempnode :
            runner=tempnode

            #we cannot get the value using tempnode.next.val so we took another
            while runner.next:
                # print("in here")
            
                if tempnode.value==runner.next.value:
                    runner.next=runner.next.next
                else:
                    runner=runner.next
            
            tempnode=tempnode.next
                
            
        return test.head


removenext=SingleLinkedList()
removenext.randomvar(10,0,20)
print(removenext)

removedupwithout(removenext)
print(removenext)

