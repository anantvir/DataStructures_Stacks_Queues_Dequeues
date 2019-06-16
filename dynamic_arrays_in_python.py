import ctypes   #Python module to create low level data structures in C (https://docs.python.org/3/library/ctypes.html#arrays)

#Amortized Analysis of Dynamic Arrays gives the intuition behind resizing logic. Reference:- 'Data Structures and Algorithms' by Michael T. Goodrich et al
class DynamicArray:
    def __init__(self):
        self.n = 0 # number of elements
        self.capacity = 1 # Intial capacity can be anything. Conventionally its 1
        self.A  = self.createNewArray(self.capacity)
    
    def __len__(self):
        return self.n

    def createNewArray(self,size):
        return (size * ctypes.py_object)()  #from ctypes documentation

    def getItem(self,index):    # get item through given index
        if not 0 <= index <= self.n:
            raise IndexError('Given index is invalid')
        return self.A[index]

    def append(self,obj):
        if self.n == self.capacity:
            self.resizeExistingArray(2*self.capacity)
        self.A[self.n] = obj
        self.n += 1 # update instance variable

    def resizeExistingArray(self,newCapacity):
        newArray = self.createNewArray(newCapacity)

        for item in range(self.n):
            newArray[item] = self.A[item]
        self.A = newArray               # assign newly created array to instance variable referencing the array i.e A
        self.capacity = newCapacity     #update instance variable 'self.capacity'  

            
