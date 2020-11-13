class ReverseIter:
    def __init__(self, items):
        self.items = items
        self.indx = 0

    def __iter__(self): 
        return self

    def __next__(self): 
        self.indx += 1
        if self.indx < len(self.items) + 1:
            return self.items[-self.indx]
            
        else:
            raise StopIteration()

