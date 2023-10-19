#pascle's triangle II
class Ri():
    def ri(self,x:int)->list[int]:
        res=[1]
        for i in range(1,x):
            new = [0]*(len(res)+1)
            for j in range(len(res)):
                new[j]+=res[j]
                new[j+1]+=res[j]
            res = new
        return res
riki=Ri()
print(riki.ri(4))