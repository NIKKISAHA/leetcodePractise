#remove color pieces if both neighbors are same color
class Ri():
    def ri(self,s:str)->bool:
        a,b=0,0
        for i in range(1,len(s)-1):
            if s[i-1]==s[i]==s[i+1]:
                if s[i]=="A":
                    a+=1
                if s[i]=="B":
                    b+=1
        return a>b
riki=Ri()
print(riki.ri("AAAABBB"))