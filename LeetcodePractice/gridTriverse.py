#grid triverse (dynamic programing)
class Ri():
    #recursion
    def ri(self,x:int,y:int)->bool:
        if ((x==1) or (y==1)):return 1
        if ((x==0) or (y==0)):return 0
        return self.ri(x-1,y)+ self.ri(x,y-1)

     #dp
    def ri(self,x:int,y:int,memo={})->bool:
        key=x,y
        if (key in memo): return memo[key]
        if ((x==1) or (y==1)):return 1
        if ((x==0) or (y==0)):return 0
        memo[key]= self.ri(x-1,y,memo)+ self.ri(x,y-1,memo)
        return memo[key]
riki=Ri()
print(riki.ri(2,3))
