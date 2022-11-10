


from random import randint


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
    

    def __str__(self):
        return str(self.value)

class SingleLinkedList:
    def __init__(self,value=None):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    
    def __str__(self):
        value=[str(x.value)  for x in self]
        return '->'.join(value)

    def __len__(self):
        node=self.head
        result=0
        while node:
            result+=1
            node=node.next
        return result
    

    def add(self,value):
        if self.head is None:
            node=Node(value)
            self.head=node
            self.tail=node
        
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
        return self.tail
    
    def randomvar(self,n,min_val,max_val):
        self.head=None
        self.tail=None
        for i in range(n):
            self.add(randint(min_val,max_val))
        return self


# Customlinked=SingleLinkedList()
# Customlinked.randomvar(10,0,99)
# print(Customlinked)
# print(len(Customlinked))