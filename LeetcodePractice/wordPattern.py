from itertools import zip_longest
class Ri():
    def ri(self,x:str,y:str)->bool:
        #solution 1 from lc, tc=sc=o(n)
        x=x.split()
        print(set(zip_longest(x,y)))
        return len(set(x))==len(set(y))==len(set(zip_longest(x,y)))
        
        #anather
        x=x.split()
        h={}
        if len(x)!=len(y):return False
        if len(set(x))!=len(set(y)):return False

        for i in range(len(x)):
            if x[i] not in h.items():
                h[x[i]]=y[i]
            elif(h[x[i]]!=y[i]):
                return False
        return True

        #anather one
        x=x.split()
        if len(x)!=len(y):return False
        h,g={},{}
        for i,j in zip(x,y):
            if i in h and h[i]!=j:return False
            if j in g and g[j]!=i:return False
            h[i]=j
            g[j]=i
        return True
    
riki= Ri()
print(riki.ri("dog cat ","bb")) 