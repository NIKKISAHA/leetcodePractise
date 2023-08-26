#length of last word
class Ri():
    def ri(self,s:str)->int:
        k=s.split()
        *a,b=k
        return len(b)
        
        #anather one
        count,l=0,len(s)-1
        while s[l] == " ":
            l -=1
        while l>0 and s[l]!=" ":
            count+=1
            l-=1
        return count

        #anather one
        c=0
        for i in range(len(s)-1,-1,-1):
                if s[i] == " ":
                     if c>0:
                          return c
                     continue
                c+=1
        return c
riki = Ri()
print(riki.ri("hello d "))