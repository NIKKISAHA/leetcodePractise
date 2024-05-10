class Ri():
    # fibonacci using recursion
    def rec(self,n:int)->list[int]:
        if n == 1: return 1
        if n == 0: return 0
        return self.rec(n-1)+self.rec(n-2)
    
    # fibonacci using top down memoization
    def rec(self,n:int)->list[int]:
        o={0:0,1:1}
        if n in o: return o[n]
        o[n]= self.rec(n-1)+self.rec(n-2)   
        return o[n]

    # fibonacci using bottom up tabulation
    def rec(self,n:int)->list[int]:
        o=[0,1]
        for i in range(2,n+1):
            p = o[i-1]+o[i-2]
            o.append(p)
        print(o)
        # return o[n] this return and next return are the same
        return o[-1]
    
    # bottom up no memory
    def rec(self,n:int)->list[int]:
        f,s=0,1
        for i in range(2,n+1):
            temp = f+s
            f=s
            s=temp
        return s
   
riki = Ri()
print(riki.rec(6))
