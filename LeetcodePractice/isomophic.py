# isomophic string 
class Ri():
    def ri(self,x:str,y:str)->bool:
        m1,m2=[],[]
        for i in x:
            m1.append(x.index(i))
            print(x.index(i))
        for j in y:
            m2.append(y.index(j))
        print(m1,m2)
        return m1==m2
         
riki= Ri()
print(riki.ri("jhii","rttg"))