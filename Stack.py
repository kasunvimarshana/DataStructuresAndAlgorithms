class Stack:
	def __init__(self):
		self.data = []

	def push(self, x):
		self.data.append(x)

	def pop(self):
		return self.data.pop()

	def empty(self):
		return len(self.data) == 0

	def __str__(self):
		return str(self.data)


if __name__ == '__main__':
    my_stack = Stack()

    my_stack.push(1)
    print("After pushing 1:  " + str(my_stack))

    my_stack.push(2)
    print("After pushing 2:  " + str(my_stack))

    my_stack.push(50)
    print("After pushing 50:  " + str(my_stack))

    my_stack.pop()
    print("After popping:  " + str(my_stack))

    my_stack.push(5)
    print("After pushing 5:  " + str(my_stack))