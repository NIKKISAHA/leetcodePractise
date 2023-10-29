#champaign tower
class Ri():
    def ri(self,pour:int,x:int,y:int)->float:
        rows=[pour]
        for i in range(1,x+1):
            newrows=[0]*(i+1)
            for j in range(i):
                extra=rows[j]-1
                if extra >0 :
                    newrows[j]+=0.5 *extra
                    newrows[j+1]+=0.5 *extra
            rows=newrows
        return min(1,rows[y])
riki=Ri()
print(riki.ri(100000009,33,17))  
