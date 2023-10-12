#find in mountain array
class Ri():
    def ri(self,x:list[int],tar:int)->int:
        m,peak=0,0
        l,r=0,len(x)-1
        while l<=r:
            m=(l+r)//2
            if (x[m-1] < x[m] < x[m+1]):
                l+=1
            elif (x[m-1] > x[m] > x[m+1]):
                r-=1
            else:
                break
        peak=m
        l,r = 0,peak
        while l<=r:
            m=(l+r)//2
            if x[m]>tar:
                r=m-1
            elif x[m]<tar:
                l=m+1
            else:
                return m
            
        l,r = peak,len(x)-1
        while l<=r:
            m=(l+r)//2
            if x[m]<tar:
                r=m-1
            elif x[m]>tar:
                l=m+1
            else:
                return m
riki=Ri()
print(riki.ri([1,2,4,5,4,3,0],0))