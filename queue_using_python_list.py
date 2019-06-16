# constant length implementation
class Queue_List:
    DEFAULT_CAPACITY = 4

    def __init__(self):
        self.Q = [None] * Queue_List.DEFAULT_CAPACITY   
        self.n = 0                                      # keep track of current number of elements in the queue. This variable will eb helpful in creating dynamic array implementation
        self.front = None                               # pointer for front of list
        self.rear = None                                #pointer for rear of list

    def enqueue(self,item):

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

    def dequeue(self):
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


        


