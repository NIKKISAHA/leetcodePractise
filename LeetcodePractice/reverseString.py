#reverse a string (string -> list[char]) 
class Ri():
    def ri(self,x:list[str])->list[str]:
        #two pointer approach
        l,r=0,len(x)-1
        while l <r:
            x[l],x[r]=x[r],x[l]
            l,r=l+1,r-1
        return x
    
        #py solution
        x[:]= x[::-1]
        return x
    
        #stack
        stack=[]
        for i in x:
            stack.append(i)
        h=0
        for i in stack:
               x[h]= stack.pop()
               h+=1
        return x

        #recurrsion
        def recuur(l,r):
             if l<r:
                  x[l],x[r]=x[r],x[l]
                  recuur(l+1,r-1)

        recuur(0,len(x)-1)
        return x
        
riki= Ri()
print(riki.ri(["h","e","l","l","o"])) 