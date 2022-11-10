


class PlateStack():
    def __init__(self,capacity):
        self.capacity=capacity
        self.stack=[]
    
    def __str__(self):
        return self.stack
    
    def push(self,item):
        if len(self.stack)> 0 and (len(self.stack[-1])) <self.capacity:
            self.stack[-1].append(item)
        else:
            self.stack.append(item)


    def pop(self):
       while len(self.stack) and len(self.stack[-1])==0:
        self.stack.pop()
        if len(self.stack)==0:
           return  None
        else:
            return self.stack[-1].pop()

    def pop_at(self,stacknumber):
        if len(self.stack[stacknumber])> 0:
            return self.stack[stacknumber].pop()
        else:
            return None




custom=PlateStack(2)
custom.push(1)
custom.push(2)
custom.push(3)
custom.push(4)
custom.push(5)
print(custom.pop())