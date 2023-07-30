#balloon word , how many times the word appears in a string
from collections import Counter
class Ri():
    def ri(self,x:str,j:str)->int:
        #solution word specific
        sum=len(x)#float("inf") 
        for i in "ban":
            sum=min(sum,x.count(i))
        print(sum)
        for i in "lo":
            sum=min(sum,x.count(i)//2)
        print(sum)    
        return sum
       
       #anather
        a=['b','a','l','o','n']
        c=[0]*5

        for i in range(5):
            c[i]=x.count(a[i])
        print(c)
        c[2]//=2
        c[3]//=2
        print(c)
        return min(c)

        #1 liner
        return min(x.count('b'),x.count('a'),x.count('l')//2,x.count('o')//2,x.count('n'))
        
        #solution
        for i in j:
            y=x.count(i)
            z=j.count(i)
            v=y//z
            print(y,z,v)
        print(y,z,v) #we have to take a min of this
        return min(v) 
        #1liner alternative
        return min(x.count(c)//j.count(c) for c in j)

        #yt solution
        t = Counter(x)
        v= Counter(j)
        res = len(j)
        for c in j:
            res=min(res,t[c]//v[c])
        return res

riki= Ri()
print(riki.ri("sjjsballonnnn","balloon")) 