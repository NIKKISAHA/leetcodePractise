#decimal to binary
class Ri():
    def ri(self,x:int,s:str="")->int:
        if x==0:
            return s
        s+=str(x%2)
        return self.ri(x//2,s)
riki=Ri()
print(riki.ri(3))