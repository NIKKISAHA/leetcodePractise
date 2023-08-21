#merge sorted array ex: x1:[1,2,4,0,0,0],x2=[2,3,4] , m1=non zero size x1=3 , m2=size=3
class Ri():
    def ri(self,x1:list[int],x2:list[int],m1:int,m2:int)->list[int]:
        l=len(x1)-1
        m1,m2=m1-1,m2-1
        print(m1,m2,l)
        while ((m1+1)>0) and ((m2+1)>0):
            if x1[m1] > x2[m2]:
                x1[l]=x1[m1]
                m1-=1
                print(x1)
            else:
                x1[l]=x2[m2]
                m2-=1
                print(x1)
            l-=1
        while ((m2+1)>0):
            x1[l]=x2[m2]
            l,m2=l-1,m2-1
        return x1
    
        #sortcut
        x1[m1:]=x2
        print(x1)
        x1.sort()
        return x1
    
        #or 
        for i in range(m1,len(x1)):
            x1[i]=x2[i-m2]
            print(i-m2)
        x1.sort()
        return x1

riki = Ri()
print(riki.ri([1,3,7,0,0,0],[1,2,4],3,3))