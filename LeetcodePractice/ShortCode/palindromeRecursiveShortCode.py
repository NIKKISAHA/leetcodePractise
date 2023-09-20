# palinfrome recursion
class Ri():
    def ri(self,s:str)->bool:
        l,r=0,len(s)-1
        if ((len(s)==0) or (len(s)==1)):
            return True
        if (s[l]==s[r]):
            return self.ri(s[1:r])
        return False
riki=Ri()
print(riki.ri("wow"))