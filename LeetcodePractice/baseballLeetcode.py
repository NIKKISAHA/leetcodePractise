#baseball game
class Ri():
    def ri(self,x:list[str])->int:
        stack=[]
        for i in x:
            if i == ("c" or "C"):
                stack.pop()
            elif i == ("d" or "D"):
                stack.append(2*stack[-1])
            elif i == "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        print(stack)
        return sum(stack)
riki= Ri()
print(riki.ri(["5","3","c","d","+"])) 