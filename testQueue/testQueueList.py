
class Queue:
    def __init__(self):
        self.items=[]
    
    def __str__(self):
        check=[str(i)  for i in self.items]
        # return str(check)
        return ''.join(check)

    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
    
    def enqueue(self,value):
        self.items.append(value)
        return "The is inserted at the end of the Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "does not contain any queue"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "does not contain any queue"
        else:
            return self.items[0]
    
    def delete(self):
        self.items=[]





    

customQueue=Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.peek())
print(customQueue.isEmpty())
print(customQueue.dequeue())
print(customQueue.delete())
print(customQueue)
