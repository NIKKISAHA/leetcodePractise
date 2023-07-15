#Can place flower ex:[1,0,0,0,1]->[1,0,1,0,1] or [0,0,1]->[1,0,1] if there's a three contigious empty slots(0) we can put a flower(1), 
# edge cases if first two elements are 0 ,ex: [0,0,1]->[1,0,1] and last two elements are 0, [1,0,0]->[1,0,1]
class Ri():
    def ri(self,x:list[int],z:int)->bool:
        # tc=O(n)
        x=[0]+x+[0] #adding 0 in begining and end for edge cases
        print(x)
        for i in range(1,len(x)):
            if x[i]==0 and x[i-1]==0 and x[i+1]==0:
                x[i]=1
                z-=1
        return z<=0
    
    #alternative solution TC=O(n)
        for i in range(len(x)):
            if x[i]==0 and (i==(len(x)-1 )or x[i+1]==0) and (i==0 or x[i-1]==0): # *1)if the number itself is 0, *2) if its the last element or next element is 0, *3)if its the first element or previos is 0
                x[i]=1
                z-=1    
        print(x)
        return z<=0
            
riki= Ri()
print(riki.ri([1,0,0],1))