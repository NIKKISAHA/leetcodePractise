#sum of highst k consecutive sum of an array [sliding window]
class Ri():
    def ri(self,x:list[int],k:int)->int:
        cursum=sum(x[0:k])
        arr=[cursum]
        
        for i in range(1,(len(x)+1)-k):
            cursum=cursum - x[i-1]
            cursum=cursum + x[i+k-1]
        #     print(cursum)
            arr.append(cursum)
        return max(arr)
riki=Ri()
print(riki.ri([10,1,2,66,3,4,5],3)) 