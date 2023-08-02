#square perfect -> 9 true ,3 false 
class Ri():
    def ri(self,x:int)->bool:
        #n/2 o(n/2)
        for i in range(1,x+1):
            if i*i==x:
                return True
            elif i*i>x:
                return False

        #binary search o(logn)   
        l,r=1,x
        while l<=r:
            mid = (l+r)//2
            if mid*mid==x:
                return True
            elif mid*mid<x:
                l=mid+1
            else:
                r=mid-1
        return False

riki= Ri()
print(riki.ri(121)) 