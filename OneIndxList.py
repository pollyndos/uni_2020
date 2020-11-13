class OneIndexedList:
    def __init__(self, arr=None):
        self.arr = arr or []

    def __getitem__(self, idx):
        return self.arr[idx-1]

    def __setitem__(self, idx, val):
        self.arr[idx-1] = val
        return val
