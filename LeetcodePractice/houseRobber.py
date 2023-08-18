#house robber
class Ri():
    def ri(self , x:list[int]):
        #yt approach
        r1,r2=0,0
        for i in x:
            temp=max(i+r1,r2)
            r1=r2
            r2=temp
            print(temp,r1,r2)
        return r2

        #leetcode apprach
        n= [0]*len(x) #[0 for _ in range(len(x))]
        # print(n)
        n[0]=x[0]
        for i in range(1,len(x)):
            inc= x[i]+n[i-2] if i-2 >=0 else x[i]
            exc= n[i-1]
            print(inc,exc)
            n[i]= max(inc, exc)
        print(n)
        return n[-1]

        # #anather approach
        n=[0]*len(x)
        n[-1]=x[-1]
        n[-2]=x[-2]
        for i in range(len(x)-3,-1,-1):
            n[i]=max(x[i],x[i]+max(n[i+2:])) #max[i+2:] = 1 max number from range i+2:rest of the array
        print(n)
        return max(n[0],n[1])
    
        #anather approach
        n=[0]*len(x)
        n[0]=x[0]
        n[1]=x[1]
        for i in range(2,len(x)):
            if i >2:
                n[i]=x[i] + max(n[i-2],n[i-3])
                print(n[i])
            else:
                n[i]=x[i]+n[i-2]
                print(n[i])

        print(n)
        return max(n[-1],n[-2])

riki=Ri()
print(riki.ri([1,2,30,3,3,1,1]))