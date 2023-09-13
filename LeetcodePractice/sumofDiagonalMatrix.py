#matrix diaganal elements sum
class Ri():
    def ri(self,x:list[int])->int:
        newlist, n = [], len(x)
        cal=0
        for i in range(len(x)):
            newlist.append(x[i][i])
            newlist.append(x[i][(len(x)-1)-i])
        for j in newlist:
            if len(x) % 2:
                if j == x[n//2][n//2]:
                     newlist.pop(i)
                     break
        return sum(cal)
        for i in range(len(x)):
            cal+=x[i][i]
            cal+=x[i][(len(x)-1)-i]
        if len(x)%2:
            cal-=x[n//2][n//2]
        return cal
riki = Ri()
print(riki.ri([[1,2,3],[4,5,6],[7,8,9]]))