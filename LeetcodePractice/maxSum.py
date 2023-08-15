#MaxSum
class Ri():
    def ri(self,x:list[int])->int:
        maxnum=x[0]
        m=0
        for i in range(len(x)):
            if m<0:
                m=0
            m+=x[i]
            maxnum=max(m,maxnum)
        return maxnum

        # nested loop
        maxnum=x[0]
        c=0
        for i in range(len(x)):
            for j in range(i+1,len(x)):
                c=x[j]+x[j]
                maxnum=max(c,maxnum)
                print(maxnum)
        return maxnum
riki=Ri()
print(riki.ri([-4,-2,0]))