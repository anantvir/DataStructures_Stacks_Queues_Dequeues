class Queue_List:
    INITITAL_CAPACITY = 4

    def __init__(self):
        self.Q = [None] * Queue_List.INITITAL_CAPACITY
        self.n = 0
        self.front = None
        self.rear = None

    def enqueue(self,item):

        if self.front==0 and self.rear == len(self.Q) - 1:
            print('Stack Overflow')
        
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
        
        return self.Q

    def dequeue(self):
        if self.front == None:
            print('Stack Underflow !')
        item = self.Q[self.front]
        self.Q[self.front] = None
        #------------Find new front--------
        if self.front == self.rear:
            self.front = None
            self.rear = None
        elif self.front == len(self.Q) - 1:
            self.front = 0
        else:
            self.front += 1
        return item

q=Queue_List()
q.enqueue(2)
q.enqueue(6)
q.enqueue(9)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()


        


