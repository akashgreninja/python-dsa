

class MultiStack:
    def __init__(self,stacksize):
        self.numberofstacks=3
        self.custList=[0]*(stacksize*self.numberofstacks)
        self.size=[0]*self.numberofstacks
        self.stacksize=stacksize
    
    def isFull(self,stacknumber):
        if self.size[stacknumber]==self.stacksize:
            return True
        else:
            return False
    
    def isEmpty(self,stacknumber):
        if self.size[stacknumber]==0:
            return True
        else:
            return False
    
    
    def indexofTop(self,stacknum):
        offset=stacknum*self.numberofstacks
        return offset+self.size[stacknum]-1

    def push(self,item,stacknum):
        if self.isFull(stacknum):
            return "The stack is Full"
        else:
            self.size[stacknum]+=1
            self.custList[self.indexofTop(stacknum)]=item

    def peek(self,stacknumber):
        if self.isEmpty(stacknumber):
            return "The stack is Full"
        else:
            value=self.custList[self.indexofTop(stacknumber)]
            return value


customStack=MultiStack(6)
print(customStack)
customStack.push(1,0)
customStack.push(2,0)
customStack.push(3,0)
customStack.push(3,0)
print(customStack.peek(0))
