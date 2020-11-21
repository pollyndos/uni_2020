class MinStack:

    def __init__(self, items=None):
        self.items = items or []
        self.mins = []
  
    def push(self, x):
        self.items.append(x)
        if len(self.mins) == 0:
            self.mins.append(x)
        elif x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        y = self.items.pop()
        if y == self.mins[-1]:
            self.mins.pop()

    def top(self):
        return self.items[-1]
    
    def getMin(self):
        return self.mins[-1]

obj = MinStack()
obj.push(-2)
obj.push(-3)
print(obj.getMin())
obj.pop()
obj.push(0)
print(obj.getMin())
print(obj.top())
