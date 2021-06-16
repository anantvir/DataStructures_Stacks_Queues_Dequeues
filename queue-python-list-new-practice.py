class QueueUsingList:

    DEFAULT_CAPACITY = 8

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        self.Q = [None] * QueueUsingList.DEFAULT_CAPACITY

    def enqueue(self,data):
        if self.front == 0 and self.rear == len(self.Q) - 1:
            raise OverflowError("Stack is overflowing !")

        #------------------- Find new rear -----------------------

        if self.front == None:      # Queue is empty
            self.front = 0
            self.rear = 0 
        elif self.rear == len(self.Q) - 1:
            self.rear = 0
        else:
            self.rear = self.rear + 1

        # ------------------- Add the item to rear of queue ----------------
        self.Q[self.rear] = data
        self.size += 1
        return self.Q
    
    def dequeue(self):
        # Check for underflow
        if self.front == None:
            raise Exception("Stack Underflow !")

        item = self.Q[self.front]
        self.Q[self.front] = None
        self.size -= 1

        # Check if front is last element
        if self.front == self.rear:
            self.front = None
            self.rear = None
        elif self.front == len(self.Q) - 1:
            self.front = 0
        else:
            self.front = self.front + 1
        return item

Q = QueueUsingList()
Q.enqueue(23)
Q.enqueue(14)
Q.enqueue(78)
Q.enqueue(49)
Q.enqueue(91)
Q.enqueue(567)
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
        