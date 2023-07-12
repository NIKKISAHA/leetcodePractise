#minstack ie stack func -> push ,pop, top, min - with O(1) time complexity
class Ri():
    stack = []
    minstack =[]
    def push(self , x:int)->int:
        self.stack.append(x)
        self.minstack.append(x if not self.minstack else min(x,self.minstack[-1]))
        return self.stack[-1]
    def pop(self)->int:
        return self.stack.pop()
    def top(self)->int:
        return self.stack[-1]
    def min(self)->int:
        return self.minstack[-1]
        
ri = Ri()
print(ri.push(1))
print(ri.push(2))
print(ri.push(5))
print(ri.push(3))
print(ri.push(10))
print(ri.pop())
print(ri.top())
print(ri.min())