#   dynamic programing min cost climbing stairs
class Ri():
    def ri(self,x:list[int])->int:
        if len(x)==1:
            return x[0]
        if len(x)<1:
            return 0
        for i in range((len(x)-3),-1,-1):
            x[i]+=min(x[i-1],x[i-2])
        return min(x[0],x[1])
riki=Ri()
print(riki.ri([15,20])) 