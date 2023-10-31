#optimal partition of a string
class Ri():
    def ri(self,s:str)->int:
        num=1
        se=set()
        for i in s:
            if i in se:
                num+=1
                se=set()
            se.add(i)
        return num
riki=Ri()
print(riki.ri("ababcaa")) 