#check if a string contain all the binary code of size k
class Ri():
    def ri(self,s:str,k:int)->bool:
        cursum=s[0:k]
        arr=set()
        arr.add(cursum)
        for i in range(1,(len(s)+1)-k):
        #     cursum= s[i:k+i] #this one line or next two lines
            cursum=cursum.removeprefix(s[i-1])
            cursum=cursum + s[i+k-1]
        #     print(cursum)
            arr.add(cursum)
        # return arr
        return len(arr)==2**k
riki=Ri()
print(riki.ri("00011011",2))