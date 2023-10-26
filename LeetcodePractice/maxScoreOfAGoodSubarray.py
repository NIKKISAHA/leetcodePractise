#max score of a good subarray
class Ri():
    def ri(self,x:int,k:int)->int:
        i=j=k
        minnum=x[k]
        maxlenarr=x[k]
        while (i>0 or (j < len(x)-1)):
            right =  x[j+1] if (j < (len(x)-1)) else 0
            left =x[i-1] if (i > 0) else 0
            if left > right:
                i-=1
                minnum=min(minnum,left)
            else:
                j+=1
                minnum=min(minnum,right)
            maxlenarr=max(maxlenarr,(minnum*(j-i+1)))
        return maxlenarr
riki=Ri()
print(riki.ri([1,4,3,7,4,5],3))

            