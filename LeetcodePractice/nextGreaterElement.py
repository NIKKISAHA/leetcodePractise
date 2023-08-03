#next gretest elment (if not found return -1) [2,3],[1,2,3]->[3,-1] (first array should be a subset of the next one)
class Ri():
    def ri(self,x:list[int],y:list[int])->list[int]:
        #tc=o(n)[whichever array is bigger] (solution from leetcode mybuddy29->thank you )
        if not x:
            return None
        d={}
        r=[]
        s=[]
        s.append(y[0])
        for i in range(1,len(y)):
            while s and y[i]>s[-1]:
                d[s[-1]]=y[i]
                s.pop()
            s.append(y[i])
        for i in s:
            d[i]=-1
        print(d)
        for i in range(len(x)):
            r.append(d[x[i]])
        return r

        #yt solution 
        index={n:i for i,n in enumerate(x)}
        print(index)
        res = [-1]*len(x)
        for i in range(len(y)):
            if y[i] not in index:
                continue
            for j in range(i+1,len(y)):
                if y[j]>y[i]:
                    ind=index[y[i]]
                    res[ind]=y[j]
                    break
        return res
riki= Ri()
print(riki.ri([2,3],[1,2,3])) 