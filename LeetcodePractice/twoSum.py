#twosum
class Ri():
    def ri(self,x:list[int],tar:int)->list[int]:
        #brute force
        # for i in range(len(x)):
        #     for j in range(i+1,len(x)):
        #         if tar==x[i]+x[j]:
        #             return [i,j]

        #hashmap
        hashm={}
        for i,n in enumerate(x):
            dif=tar - n
            if dif in hashm:
                return [i,hashm[dif]]
            hashm[n]=i
riki=Ri()
print(riki.ri([1,2,3],5))