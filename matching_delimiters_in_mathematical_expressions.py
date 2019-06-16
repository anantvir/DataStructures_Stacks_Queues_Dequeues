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
        if not self.isEmpty():
            return self.data[-1]
        else:
            raise StackEmpty('Stack is Empty !')
    
    def pop(self):
        if not self.isEmpty():
            return self.data.pop()     # use inbuilt python method
        else:
            raise StackEmpty('Stack is Empty !')

# Processing mathematical expressions to make sure their delimiting symbols matchup correctly
def matching_delimiters(expression):
    left_symbols = '({['
    right_symbols = ')}]'

    stack = StackUsingList()

    for each_character in expression:
        if each_character in left_symbols:
            stack.push(each_character)
        
        elif each_character in right_symbols:
            if stack.isEmpty():
                raise Exception('Stack is Empty !')
            
            if right_symbols.index(each_character) == left_symbols.index(stack.pop()):
                return True
    return stack.isEmpty()

