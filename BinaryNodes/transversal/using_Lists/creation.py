
class BinaryTree:
    def __init__(self, size):
        self.customList = size*[None]
        self.lastusedindex = 0
        self.maxsize = size


 


    def insert(self, value):
        if self.lastusedindex + 1 == self.maxsize:
            return "binary tree is full"
        self.customList[self.lastusedindex+1] = value
        self.lastusedindex += 1
        return "done"


    def search(self, value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return "sucess"
        return "Not found"

    def preOrderList(self, index):
        # nlr
        if index > self.lastusedindex:
            return
        print(self.customList[index])
        self.preOrderList(index*2)
        self.preOrderList((index*2)+1)
# why this is coming reverse is because we have stored multiple values in return and printing it all at once
    def InOrderList(self, index):
        # lnr
        if index > self.lastusedindex:
            return
        self.InOrderList(index*2)
        print(self.customList[index])
        
        self.InOrderList(index*2+1)

          
    def deleteBT(self):
        self.customList=None
        self.lastusedindex=0

    def PostOrderList(self, index):
        # lrn
        if index > self.lastusedindex:
            return
        self.PostOrderList(index*2)
       
        
        self.PostOrderList(index*2+1)
        print(self.customList[index])


    def LevelOrderList(self, index):
        # nlr
        for i in range(index,self.lastusedindex+1):
            print(self.customList[i])

      
    def DeleteNode(self, thenode):
        if self.lastusedindex==0:
            return "No elements"
       
        for i in range(len(self.customList)):
            if self.customList[i]==thenode:
                self.customList[i]=self.customList[self.lastusedindex]
                self.customList[self.lastusedindex]=None
                self.lastusedindex-=1
                return"sucess"
         


   
      
     

        
      
      
        
        
       


test = BinaryTree(8)

# as this is linked list with the formula being[2x ] and [2x+1] for left abd right node we just add the nodes
test.insert("DRINKS")
test.insert("Hot")
test.insert("Cold")
test.insert("tea ")
test.insert("Coffee")

# test.search("Coffee")
# test.preOrderList(1)
# test.InOrderList(1)
# test.PostOrderList(1)
# test.LevelOrderList(1)
# print(test.DeleteNode("Coffee"))
test.deleteBT()
test.LevelOrderList(1)