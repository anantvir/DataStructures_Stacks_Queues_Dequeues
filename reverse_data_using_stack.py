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



# Read lines of file and print them in reverse order
def reverse_lines(file_path):
    stack = StackUsingList()
    read_file = open(file_path,'r')
    for eachLine in read_file:
        stack.push(eachLine)
    read_file.close()

    #Write the stack contents back to file
    output_file = open(file_path,'w')
    while not stack.isEmpty():
        output_file.write(stack.pop())
    output_file.close()



pth= 'C:\\Users\\anant\\Desktop\\DS_Algo\\ReverseDataUsingStack\\test.txt'
reverse_lines(pth)