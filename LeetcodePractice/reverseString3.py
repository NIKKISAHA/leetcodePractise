#reverse words in a string 3
class Ri():
    def ri(self,s:str)->str:
       s=list(s)
       l=0
       for r in range(len(s)):
           if s[r]==" " or r == len(s)-1:
                templ,tempr=l,r-1

                if r == len(s)-1:
                        templ,tempr=l,r
                while templ<tempr:
                     s[tempr],s[templ]=s[templ],s[tempr]
                     tempr-=1
                     templ+=1
                l=r+1
       return "".join(s)
        
    #anather
    #    return " ".join([w[::-1] for w in s.split()])
    

    #anather
        # w=[w[::-1] for w in s.split()]
        # return " ".join(w)
riki=Ri()
print(riki.ri("apple is good"))