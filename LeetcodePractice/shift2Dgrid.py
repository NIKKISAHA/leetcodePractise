#shift 2D grid
class Ri():
    def ri(self,x:list[list[int]],k:int)->list[list[int]]:
        m,n = len(x),len(x[0])

        def d2dTo1d(r,c): #2d to 1d
                return r*n+c
        def d1dTo2d(i): #1d to 2d
                return [i//n,i%n]
        res = [[0]*n for i in range(m)] #making a new list
        
        for r in range(m):
              for c in range(m):
                    newindex=(d2dTo1d(r,c)+k)%(m*n) #2d to 1d
                    newr,newc=d1dTo2d(newindex) #1d to 2d
                    res[newr][newc]=x[r][c] #mapping
        return res
    
        #anather solution
        l=[n for row in x for n in row]  #2d to 1d
        print(l)
        m,n = len(x),len(x[0])
        k=k%(m*n)
        l=l[-k:]+l[:-k] #shift k element
        print(l)
        return [l[i*n:i*n+n]for i in range(m)] #1d to 2d
riki= Ri()
print(riki.ri([[2,3,4],[4,5,9]],3))