#sign of product of an array
class Ri():
    def ri(self,x:list[int])->int:
        if len(x)==0:return 0
        count=0
        for i in x:
            if i == 0:
                return 0 
            elif i <0:
                count+=1
        return 1 if count % 2 ==0 else -1
riki=Ri()
print(riki.ri([-90]))