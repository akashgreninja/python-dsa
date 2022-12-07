
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

    def __str__(self):
        # print(self.value)
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next


class Queue:
    def __init__(self):
        self.LinkedList=LinkedList()
    
    def __str__(self):
        values =[str(i) for i in self.LinkedList]
        print(values)
        return ' '.join(values)

    def enqueue(self,value):
        node=Node(value)
        if self.LinkedList.head==None:
            self.LinkedList.head=node
            self.LinkedList.tail=node
        
        else:
            self.LinkedList.tail.next=node
            self.LinkedList.tail=node


    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False


    def Enqueue(self):
        if self.isEmpty():
            return "queue is empty"
        else:
            tempnode=self.LinkedList.head
            if self.LinkedList.head==self.LinkedList.tail:
                self.LinkedList.head=None
                self.LinkedList.head=None
            else:
                self.LinkedList.head=self.LinkedList.head.next
            return tempnode
    

    def peek(self):
        if self.isEmpty():
            return "queue is empty"
        else:
            return self.LinkedList.head


    def delete(self):
       
       
    
        self.LinkedList.head=None
        self.LinkedList.tail=None



# checklist=Queue()
# checklist.enqueue(1)
# checklist.enqueue(2)
# checklist.enqueue(3)
# checklist.enqueue(4)
# print(checklist)
# checklist.Enqueue()
# print(checklist)
# print(checklist.isEmpty())
# print(checklist.peek())
