# This code shows how to use Stack ADT to match tags in HTML document. This concept is used to validate tags in any markup language

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


def match_tags(row):        #input is each row of the HTML file
    S = StackUsingList()
    i = row.find('<')
    if i == -1:
        return False
    
    while i != -1:
        k = row.find('>',i+1)
        if k == -1:
            return False
        tag = row[i+1,k]
        if not tag.startswith('/'):     #https://www.tutorialspoint.com/python/string_startswith.htm
            S.push(tag)                 #push tags on stack and then pop and compare with the tag which contains '/'. If both are same then tags match
        else:
            if tag.isEmpty():
                return False
            if tag[1:] != S.pop():
                return False
        i = row.find('<',k+1)
    return S.isEmpty()                  # if stack is empty, it means that all tags matched !          

