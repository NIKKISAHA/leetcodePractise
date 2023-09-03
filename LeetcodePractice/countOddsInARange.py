#count odds in a range
class Ri():
    def ri(self,l:int,r:int)->int:
        diff=(r-l)//2
        print(diff)
        if l%2==0 and r%2==0:
            return diff
        return diff+1
    
        #anather way
        lenth=r-l+1
        odd=lenth//2
        if lenth %2 ==1 and l%2 ==1:
            return odd+1
        return odd
    
        #one line
        return ((r+1)//2) - (l//2)
riki = Ri()
print(riki.ri(1,5))