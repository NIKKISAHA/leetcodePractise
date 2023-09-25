#diffence between array
class Ri():
    def ri(self,x:str,y:str)->str:
        if (len(x) ==0) and (len(y) ==0 ):return 0
        r ,q=set(x),set(y)
        if len(r) > len(q):
            q,r=r,q
        
        for i in r:
            if i in q:
                q.remove(i)
        return q

        #anather one
        x,y = list(x),list(y)
        if len(y) > len(x):
            x,y=y,x
        for i in y:
            if i in x:
                x.remove(i)
        return str(x)

        #for one character difference
        sum_1,sum_2=0,0

        for i in x:
            sum_1+=ord(i)
        for i in y:
            sum_2+=ord(i)
        return chr(sum_2-sum_1) if (sum_2>sum_1) else chr(sum_1-sum_2) 

        #for one character difference
        res=0
        for i in x:
            res^=ord(i)
        for i in y:
            res^= ord(i)
        return chr(res)
        
riki=Ri()
print(riki.ri("","7")) 
        
