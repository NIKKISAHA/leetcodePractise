#decode ways
class Ri():
    def ri(self,x:str)->int:
        dp bottom up
        a,b=1,1
        for i in range((len(x)-1),-1,-1):
            n=0
            if x[i]=="0":
                a=0
            else:
                n+=a
            if (((i+1)<len(x))and (x[i]=="1" or ((x[i]=="2") and (x[i+1] in "0123456")))):
                n+=b
            a,b=n,a
        return a
        
        #dp using cache
        dp={len(x):1}
        for i in range((len(x)-1),-1,-1):
            if x[i]=="0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]
            if (((i+1)<len(x))and (x[i]=="1" or ((x[i]=="2") and (x[i+1] in "0123456")))):
                dp[i]+=dp[i+2]
        return dp[0] 

        #using recursion
        dp={len(x):1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if x[i]=="0":
                return 0
            res=dfs(i+1)
            if (((i+1)<len(x))and (x[i]=="1" or ((x[i]=="2") and (x[i+1] in "0123456")))):
                res+=dfs(i+2)
            dp[i]=res
            return res
        return dfs(0)       
riki=Ri()
print(riki.ri("12")) 