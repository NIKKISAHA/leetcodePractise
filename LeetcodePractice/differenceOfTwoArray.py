#find difference of two array [1,2,3],[2,9,8] -> [1,3],[9,8]
class Ri():
    def ri(self,x:list[int],y:list[int])->list[list[int]]:
        set1,set2=set(x),set(y)
        set3,set4=set(),set()
        for i in set1:
            if i not in set2:
                set3.add(i)
        for j in set2:
            if j not in set1:
                set4.add(j)
        return [list(set3),list(set4)]

        #anather one
        set1,set2=set(x),set(y)
        set3,set4=set(),set()
        set3=list(set1-set2)
        set4=list(set2-set1)
        return [set3,set4]

riki = Ri()
print(riki.ri([1,2],[9]))