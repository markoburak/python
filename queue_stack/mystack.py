class MyStack(object):

    def __init__(self):
        self.arr = []

    def get(self):
        print(self.arr)
        return self.arr

    def add(self,arg):
        self.arr.append(arg)
        return self.arr

    def remove(self):
        self.arr.pop()
        return self.arr

