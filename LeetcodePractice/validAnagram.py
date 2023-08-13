#valid anagram
class Ri():
    def ri(self,s:str,x:str)->bool:
        return sorted(s) == sorted(x)
    
        return set(s)==set(x)
    
        hash1,hash2={},{}
        for i in range(len(s)):
            hash1[s[i]]=1+hash1.get(s[i],0)
            hash2[x[i]]=1+hash2.get(x[i],0)
        for i in hash2:
            if hash2[i] != hash1.get(i,0):
                return False
        return True
    
riki=Ri()
print(riki.ri("cat","tar"))