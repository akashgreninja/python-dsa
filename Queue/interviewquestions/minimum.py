
class Node():
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
    
    def __str__(self):
        node=str(self.value)
        if self.next:
            node+=','+ str(self.next)
        return node
    
class Stack():
    def __init__(self):
        self.top=None
        self.min=None
    
    def minimum(self):
        if not self.min:
            return None
        else:
            return self.min.value
        
    def push(self,value):
        if self.min and (self.min.value <value):
            self.min=Node(value=self.min.value,next=self.min)

        else:
            self.min=Node(value=value,next=self.min)
        self.top=Node(value=value,next=self.top)


    def pop(self):
        if self.top==None:
            return None
        self.min=self.min.next
        item=self.top.value
        self.top=self.top.next
        return item



custom=Stack()
custom.push(3)
print(custom.minimum())
custom.push(2)
print(custom.minimum())
custom.push(1)
print(custom.minimum())
custom.pop()
print(custom.minimum())
