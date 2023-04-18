class Stack:
    def __init__(self) -> None:
        self.items=[]
    def pop(self):
        self.items.pop()
    def push(self,item):
        self.items.append(item)
    def peek(self):
        return self.items[-1]
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)