#MaxSum
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
        m=0

        # nested loop
        maxnum=x[0]
        
        for i in range(len(x)):
            c=x[i]
            for j in range(i+1,len(x)):
                print(c)
                c+=x[j]
                maxnum=max(c,maxnum)
                # print(maxnum)
        return maxnum
riki=Ri()
print(riki.ri([2,-8,0]))
