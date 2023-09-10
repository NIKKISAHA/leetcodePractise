#merge two array alternively
class Ri():
    def ri(self,x:list[int],y:list[int])->list[int]:
        if len(y)==0 and len(x)==0 :return 0
        if len(x)==0 : return y
        if len(y)==0 : return x

        z=[]
        if len(x)<len(y):
                for i in range(len(x)):
                     z.append(x[i])
                     z.append(y[i])
                lenth = len(x)
                for j in range(lenth,len(y)):
                     z.append(y[j])
        else:
                for n in range(len(y)):
                     z.append(x[n])
                     z.append(y[n])
                lenth = len(y)
                for m in range(lenth,len(x)):
                     z.append(x[m])
        return z
riki = Ri()
print(riki.ri([2,3],[1,0]))