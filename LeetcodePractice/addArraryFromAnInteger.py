#add array form an integer
class Ri():
    def ri(self,x:list[int],k:int)->list[int]:
        s=""
        for i in x:
            s+=str(i)
        a=int(s)
        a+=k
        a=str(a)
        l=len(a)
        p=[]
        for i in range(l):
          p.append(int(a[i]))
        return p
        #alternative
        # x.reverse()
        # i = 0
        # while k:
        #     d=k%10
        #     if i < len(x):
        #         x[i]+=d
        #     else:
        #         x.append(d)
            
        #     add=x[i]//10
        #     x[i]%=10

        #     k//=10
        #     k+=add
        #     i+=1
        # x.reverse()
        # return x
            
riki=Ri()
print(riki.ri([1,2,7,4],181))      