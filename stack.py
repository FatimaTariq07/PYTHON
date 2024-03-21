class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None


if __name__ == "__main__":

    stk = Stack()
    stk.push(20)
    stk.push(30)
    stk.push(40)
    stk.push(50)
    stk.push(60)
    print(stk.stack)
    print(stk.pop())
    print(stk.stack)
    print(stk.pop())
    print(stk.pop())
    print(stk.pop())
    print(stk.pop())
    print(stk.stack)
    print(stk.is_empty())
    print(stk.peak())