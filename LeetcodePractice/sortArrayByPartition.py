# sort array by partition
class Ri():
    def ri(self,x:list[int])->list[int]:
        l=0
        for r in range(len(x)):
            if x[r]%2==0:
                x[l],x[r]=x[r],x[l]
                l+=1
        return x
riki=Ri()
print(riki.ri([1,2,4,8]))  