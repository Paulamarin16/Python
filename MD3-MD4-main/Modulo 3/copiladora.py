class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self,inicial=0):
        Stack.__init__(self)
        self.numero=inicial

    def get_counter(self):
        return self.numero

    def pop(self):
        self.numero += 1
        return self.numero


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
