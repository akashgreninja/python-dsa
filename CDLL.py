

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create(self, value):
        newnode = Node(value)
        newnode.prev = self.tail
        newnode.next = self.tail
        self.head = newnode
        self.tail = newnode

    def insert(self, value, location):
        if self.head == None:
            print("node does not exist")

        else:
            newnode = Node(value)
            if location == 0:
                newnode.prev = self.tail
                newnode.next = self.head
                self.head = newnode
                self.head.prev = newnode
                self.tail.next = newnode

            elif location == -1:
                newnode.prev = self.tail
                newnode.next = self.head

                self.tail.next = newnode
                self.tail = newnode
                self.head.prev = self.tail.next
                # self.head.prev=newnode (both the lines give same result)

            else:
                tempnode = self.head
                index = 0
                while index < location-1:
                    tempnode = tempnode.next
                    index += 1

                nextnode = tempnode.next
                newnode.prev = tempnode
                newnode.next = nextnode
                tempnode.next = newnode
                nextnode.prev = newnode

    def transversal(self):
        node = self.head

        while node:
            print(node.value)

            if node == self.tail:

                break
            node = node.next

    def reversetransversal(self):
        if self.head is None:
            print("not possible")
        else:
            node = self.tail

            while node:
                print(node.value)

                if node == self.head:

                    break
                node = node.prev

    def search(self, value):
        if self.head is None:
            print("not possible")
        else:
            node = self.head

            while node:
                if node.value == value:
                    print("foundd")

                if node == self.tail:

                    break
                node = node.next



    def delete(self,location):

        if self.head == None:
            print("node does not exist")
        
        else:
            if location==0:
                if self.head==self.tail:
                    self.tail=None
                    self.head=None
                    self.head.prev=None
                    self.head.next=None
                
                else:
                    self.head=self.head.next
                    self.tail.prev=self.tail
                    self.tail.next=self.head
                    
            
            elif location==-1:
                if self.head==self.tail:
                    self.tail=None
                    self.head=None
                    self.head.prev=None
                    self.head.next=None
                else:
                   
                    # as soon as we do self.tail the node gets changed to the previous one so then self.next.tail is ert to the previous one
                    self.tail=self.tail.prev
                    self.tail.next=self.head
                    self.head.prev=self.tail
            
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=nextnode.next


    def deleteall(self):
        self.tail.next=None
        node=self.head
        while node is not None:
            node.prev=None
            node=node.next
          
            
        self.head=None
        self.tail=None
            
      


CircularLinkedList = CDLL()
CircularLinkedList.create(1)
CircularLinkedList.insert(2, 0)
CircularLinkedList.insert(3, 1)
CircularLinkedList.insert(4, -1)


print([node.value for node in CircularLinkedList])
CircularLinkedList.transversal()
CircularLinkedList.reversetransversal()
CircularLinkedList.search(4)
CircularLinkedList.delete(-1)
print([node.value for node in CircularLinkedList])
CircularLinkedList.deleteall()
print([node.value for node in CircularLinkedList])

