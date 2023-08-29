#square root find
class Ri():
    def ri(self,x:int)->int:
        # if x<2:
        #     return x
        l,r=0,x-1
        while l<r:
            mid = (l+r)//2
            if mid*mid  == x: #or (x//mid)
                return mid
            elif mid*mid > x:
                r=mid-1
            else:
                l=mid+1
        return l
    
        #brute force approach
        r=0
        while r*r <=x:
        #     print(r*r)
            r+=1
        return r-1
riki = Ri()
print(riki.ri(8))