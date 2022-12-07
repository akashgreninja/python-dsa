

class testQueuelimit:
    def __init__(self, limit):
        self.list = [None]*limit
        self.limit = limit
        self.top = -1
        self.start = -1

    def __str__(self):
        check = [str(i) for i in self.list]

    def isEmpty(self):
        if self.top == -1:
            return True

    def isFull(self):
        if self.start == 0 and self.top+1 == self.limit:
            return "is full"
        elif self.top+1 == self.start:
            return "is full"

    def enqueue(self, value):
        if self.isFull():
            return 'The queue is Full'
        else:
            if self.top+1 == self.limit:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            return 'The queue is Full'
        else:
            firstelement = self.limit[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1

            elif self.start+1 == self.limit:
                self.start = 0
            else:
                self.start += 1
            self.limit[start] = None
