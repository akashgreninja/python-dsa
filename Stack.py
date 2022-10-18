

class testStack:
    def __init__(self):
        self.stack=[]

    def __str__(self):
        values=self.stack.reverse()
        value=[str(x)   for x in self.stack]
        return '\n'.join(value)

    def isempty(self):
        if self.stack==[]:
            return True
        
    def push(self,value):
        self.stack.append(value)

    def peek(self):
        return self.stack[len(self.stack)-1]
            
        

check=testStack()
check.push(1)
check.push(2)
check.push(3)
print(check.peek())
print(check)