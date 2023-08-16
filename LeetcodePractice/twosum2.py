#twosum2 in sorted array, two pointer approach 
class Ri():
    def ri(self,x:list[int],tar:int)->list[int]:
        l,r=0,len(x)-1
        while l<r:
            cur=x[l]+x[r]
            if cur == tar:
                return [l+1,r+1]
            elif cur > tar:
                r-=1
            else:
                l-=1
        return -1
riki=Ri()
print(riki.ri([2],5))