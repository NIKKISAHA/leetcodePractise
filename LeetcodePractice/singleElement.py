#single element ,the array given consists of every element appearing twice except for one ex:[3,1,3]->1
from functools import reduce
class Ri():
    def ri(self,x:list[int])->int:
        #using a dict tc=o(n) sc=o(n)
        d={}
        for i in x:
            if i not in d:
                d[i]=True
            else:
                d[i]=False
        for key,value in d.items():
            if value==True:
                return key
        return -1

        #anather solution using reduce (see the definition from brocode) it's using lamba and bitwise xor (^used for xor)
        return reduce(lambda z,y:z^y,x)
        
        #anather solution 2*sum - sum =number (since each num has appeared twice)
        return 2*(sum(set(x)))-sum(x)
        
        #anather xor
        xor=0
        for i in x:
            xor=xor^i
        return xor
riki= Ri()
print(riki.ri([4,2,2,4,6,1,1,4,4])) 