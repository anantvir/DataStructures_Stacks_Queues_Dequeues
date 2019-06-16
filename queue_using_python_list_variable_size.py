# This code uses concept of modular arithemetic for calculation of new front and rear indexes- from book 'DS Algo by Michael T. Goodrich et al'
class Queue_List:
    INITIAL_CAPACITY = 5

    def __init__(self):
        self.Q = [None] * Queue_List.INITIAL_CAPACITY
        self.size = 0
        self.front = 0
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

    def first(self):    # return but do not remove front of the queue
        if self.isEmpty():
            print('Queue is empty !')
        return self.Q[self.front]
    
    def enqueue(self,item):
        if self.size == len(self.Q):
            self.resize(2*len(self.Q))
        new_rear = (self.front + self.size)%len(self.Q)        # from 'DS Algo in Python by Michael T Goodrich'
        self.Q[new_rear] = item
        self.size += 1
    
    def resize(self,new_capacity):
        old_list = self.Q
        self.Q = [None] * new_capacity
        front_pointer = self.front

        for x in range(self.size):
            self.Q[x] = old_list[front_pointer]
            front_pointer = (1 + front_pointer)%len(old_list)     # from 'DS Algo in Python by Michael T Goodrich'
        self.front = 0                                          # set front = 0 for the newly created list

    def dequeue(self):
        item = self.Q[self.front]
        self.Q[self.front] = None                               # will be cleaned by garbace collector
        self.front = (self.front + 1) % len(self.Q)
        self.size -= 1
        return item

q = Queue_List()
q.enqueue(2)   