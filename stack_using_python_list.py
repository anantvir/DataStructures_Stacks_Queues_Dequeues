class StackEmpty(Exception):
    pass

class StackUsingList:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0
    
    def push(self,value):
        self.data.append(value)
    
    def top(self):
        if not self.isEmpty:
            return self.data[-1]
        else:
            raise StackEmpty('Stack is Empty !')
    
    def pop(self):
        if not self.isEmpty:
            self.data.pop()     # use inbuilt python method
        else:
            raise StackEmpty('Stack is Empty !')