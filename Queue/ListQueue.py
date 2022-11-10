class Queue:
    def __init__(self,maxSize):
        self.items=maxSize*[None]
        self.maxSize=maxSize
        self.top=-1
        self.start=-1 
    
    def __str__(self):
        values=[str(i) for i in self.items]
        return ''.join(values)
    
    def isFull(self):
        if self.top+1==self.start:
            return True
        elif self.start==0 and self.top+1==self.maxSize:
            return True
        else: 
            return False

    
    def isEmpty(self):
        if self.top==-1:
            return True
        
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return 'The queue is Full'
        else:    
            if self.top+1==self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
            self.items[self.top]=value

    def dequeue(self):
        if self.isEmpty():
            return"no element"
        
        else:
            firstelement=self.items[self.start]
            start=self.start
            if self.start==self.top:
                self.start=-1
                self.top=-1
            elif self.start+1==self.maxSize:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return firstelement

            
    def peek(self):
        if self.isEmpty():
            return"no element"
        else:
            return self.items[self.start]
        

    def delete(self):
        self.items=self.maxSize*[None]
        self.top=-1
        self.start=-1


customqueue=Queue(3)

customqueue.enqueue(1)
customqueue.enqueue(2)
customqueue.enqueue(3)
print(customqueue.peek())
print(customqueue)
customqueue.dequeue()
# print(customqueue.isEmpty())
print(customqueue)
customqueue.delete()
print(customqueue)
