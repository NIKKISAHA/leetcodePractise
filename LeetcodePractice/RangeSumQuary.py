#sliding window ->range sum quary immutable
class Ri():
        def ri(self,l:int,r:int,x:list[int])->int:
                newarray = []
                sum = 0
                for i in x:
                        sum+=i
                        newarray.append(sum)
                
                print(newarray)
                return (newarray[r] - newarray[l-1]) if l>0 else newarray[r]
riki = Ri()
print(riki.ri(0,5,[1,2,3,4,5,9]))