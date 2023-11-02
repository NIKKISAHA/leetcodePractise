#longest consequtive sequence
class Ri():
    def ri(self,x:list[int])->int:
        maxleng=0
        newset =set(x)
        for i in newset:
            if (i-1) not in newset:
                leng=0
                while (i+leng) in newset:
                    leng+=1
                maxleng=max(leng,maxleng)
        return maxleng
riki=Ri()
print(riki.ri([1,3,2,0,100,200,201,203,204,202])) 