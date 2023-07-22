# index of the first occurance of the anather string
class Ri():
    def ri(self,x:str,y:str)->int:
        # for i in range(len(x)+1-len(y)):
        #     print(x[i:i+len(y)])
        #     if x[i:i+len(y)]==y:
        #         print(x[i:i+len(y)])
        #         return i
        # return -1

        # using two pointer 
        l,r=0,len(y)
        while r <= len(x):
            if x[l:r]==y:
                return l
            l+=1
            r+=1
        return -1
riki= Ri()
print(riki.ri("nmmokommm","ok")) 