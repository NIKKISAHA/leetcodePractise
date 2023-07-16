#valid palindrome ignoring special characters and space
class Ri():
   #solution TC=O(n)
   def s(self,ri:str)->bool:
    ri=ri.lower()
    for i in ri:
        if i.isalnum()==False:
          ri=ri.replace(i,"")
    return list(ri)== list(reversed(ri))
   
    #anather solution TC=O(n)
    ri=[c.lower() for c in ri if c.isalnum()]
    return ri==ri[::-1]
          
riki= Ri()
print(riki.s("12"))