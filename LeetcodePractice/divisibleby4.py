#divisible by 4
import math
class Ri():
    def ri(self,x:int)->bool:
        print((math.log(4,4)%1))
        return False if x <=0 else math.log(x,4) % 1  == 0

        #recursive
        if x==0:
            return True
        if x <=0 or x%4:
            return False
        return self.ri(x//4)
riki=Ri()
print(riki.ri(14))