#k-th symbol in grammer
class Ri():
    def ri(self,x:int,k:int)->int:
        cur=0
        l,r=1,2**(x-1)
        while l<=r:
            mid =( l+r)//2
            if(mid >= k):
                r=mid-1
            else:
                l=mid+1
                cur = 0 if (cur==1) else 1
        return cur
riki=Ri()
print(riki.ri(4,3))   