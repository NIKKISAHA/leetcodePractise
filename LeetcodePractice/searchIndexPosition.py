#serch index positon ####

import bisect #this is only for the bisect solution - O(1)
class Ri():
    def ri(self,x,target:int)->int:
        l,r=0,len(x)

#         # solution 1 logn
        while l <=r:
            mid= (l+r)//2
            if len(x)==1:
                if x[0] < target:
                 return 1
                break
            if (target==x[mid]):
                return mid
            elif target > x[mid]:
                l=mid+1
            else:
                r=mid-1 
        return l

        #solution 2 logn
        while l < r:
            mid = (l+r)//2
            print(mid)
            if target >x[mid]:
                l= mid +1 
            else:
                r=mid
        return l

        # o(n) solution
        for i ,j in enumerate(x):
            print(j)
            if j>=target:
                return i
        return len(x)

        #o(1) solution using bisect
        return bisect.bisect_left(x,target)

riki= Ri()
print(riki.ri([1,2],5))