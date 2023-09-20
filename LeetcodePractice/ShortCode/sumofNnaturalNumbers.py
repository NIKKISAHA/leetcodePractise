#sum of n natural numbers
class Ri():
    def ri(self,x:int)->int:
        if x==0:
            return x
        return x + self.ri(x-1)     
riki=Ri()
print(riki.ri(3))