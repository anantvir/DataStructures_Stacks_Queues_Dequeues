class DoubleEndedQueue:

    INITIAL_CAPACITY = 5

    def __init__(self):
        self.Q = [None] * DoubleEndedQueue.INITIAL_CAPACITY
        self.n = 0
        self.front = None
        self.rear = None

    def __len__(self):
        return self.n

    def enqueue_rear(self,item):

        if self.front==0 and self.rear == len(self.Q) - 1:
            print('Overflow')      
        #------------find new rear-----------
        if self.rear == len(self.Q) - 1:
            self.rear = 0
        elif self.front == None:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        #--------------------------------------
        self.Q[self.rear] = item
        self.n += 1       
        return self.Q
    
    def enqueue_front(self,item):
        if self.front == None:
            self.front = 0
            self.rear = 0
        if self.front == 0 and self.rear == len(self.Q) - 1:
            print('Overflow !')

        if self.front == 0:
            self.front = len(self.Q) - 1
        else:
            self.front -= 1      
        self.Q[self.front] = item
        self.n += 1
        return self.Q
        
    def dequeue_front(self):
        if self.front == None:
            print('Underflow !')
        item = self.Q[self.front]
        self.Q[self.front] = None
        self.n -= 1
        #------------Find new front--------
        if self.front == self.rear:
            self.front = None
            self.rear = None
        elif self.front == len(self.Q) - 1:
            self.front = 0
        else:
            self.front += 1
        return item

    def dequeue_rear(self):
        if self.front == None:
            self.front = 0
            self.rear = 0
        if self.front == len(self.Q) - 1 and self.rear == len(self.Q) - 1:
            item = self.Q[self.rear]
            self.Q[self.rear] = None
            self.rear = None
            self.front = None
        else:
            item = self.Q[self.rear]
            self.Q[self.rear] = None
            self.rear -= 1
        return item
   
q = DoubleEndedQueue()
q.enqueue_rear(2)
q.enqueue_rear(5)
q.enqueue_rear(9)

q.dequeue_rear()
q.dequeue_rear()