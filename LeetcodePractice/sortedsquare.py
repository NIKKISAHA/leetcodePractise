class Ri():
    def ri(self,x:list[int])->int:
        for i in range(len(x)):
            x[i]*=x[i]
        x.sort()
        return x

        #anather
        return sorted([i**2 for i in x])

        #anather
        l,r=0,len(x)-1
        n=[None] * len(x)
        for i in range(len(x)-1,-1,-1):
            if abs(x[l])>abs(x[r]):
                n[i]=x[l]**2
                l+=1
            else:
                n[i]=x[r]**2
                r-=1
        return n
riki= Ri()
print(riki.ri([-1,-2,2,3,5,5])) 