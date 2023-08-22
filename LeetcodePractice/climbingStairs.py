#climing stairs
class Ri():
    def ri(self,x:int)->int:
        last,secondlast=1,1
        for i in range(x+1,2,-1): #range(x,1,-1) -> the range is same
            print(i)
            temp=last
            last=last+secondlast
            secondlast=temp
        return last

        #similar
        if x<1:
            return 1
        dp=[0]*(x+1)
        dp[0],dp[1]=1,1       
        for i in range(2,x+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[x]

        # #fibonacci series TC=2^n
        if x==1 or x==0:
            return 1
        return self.ri(x-1)+self.ri(x-2)
riki = Ri()
print(riki.ri(0))