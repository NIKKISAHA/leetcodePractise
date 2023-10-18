#pascles triangle
class Ri():
    def ri(self,x:int)->list[list[int]]:
        lis=[[1]]
        for i in range(x-1):
            temp=[0]+lis[-1]+[0]
            new=[]
            for j in range(len(lis[-1])+1):
                k=temp[j] + temp[j+1]
                new.append(k)
            lis.append(new)
        return lis
riki=Ri()
print(riki.ri(4))