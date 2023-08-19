#best time to buy and sell stocks
class Ri():
    def ri(self,x:list[int])->int:
        #easy approach
        minp,maxp=float("inf"),0
        for i in range(len(x)):
            minp=min(minp,x[i])
            if x[i]>=minp:
                maxp=max(maxp,x[i]-minp)
        return maxp

        #yt approach
        l,r,maxP=0,1,0
        while r < len(x):
            if x[r]>x[l]:
                p=x[r]-x[l]
                maxP=max(maxP,p)
            else:
                l=r
            r+=1
        return maxP
riki=Ri()
print(riki.ri([1,2,30,3,3,1,1]))