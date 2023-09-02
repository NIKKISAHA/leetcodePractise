#contain duplicates 2
class Ri():
        def ri(self,x:list[int],k:int)->bool:
                newset=set()
                l=0
                for i in range(len(x)):
                        if (i-l)>k:
                                newset.remove(x[l])
                                l+=1
                                print(x[l])
                        if x[i] in newset:
                                return True
                        newset.add(x[i])
                return False
                
riki = Ri()
print(riki.ri([1,2,4,9,10,1],2))