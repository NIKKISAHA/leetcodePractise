#shuffle of array-> [x,x,x,y,y,y,y]->[x,y,x,y,x,y,x,y]
class Ri():
    def ri(self,x:list[int],k:int)->list[int]:
        newlist=[]
        for i in range(k):
            newlist.append(x[i])
            newlist.append(x[k+1])
        return newlist
    
        newlist=[0*i for i in range(2*k)]
        for i in range(k):
            newlist[(2*i)]=x[i]
            newlist[(2*i)+1]=x[k+i]
        return newlist
riki = Ri()
print(riki.ri([2,2,2,6,6,6],3))