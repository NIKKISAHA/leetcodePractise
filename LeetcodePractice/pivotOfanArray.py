# pivot of an array -> left side sum, number, right side sum, ex :[5,3,2]->5 index = 0
class Ri():
    def ri(self,x:list[int])->int:
        sum=0
        l=0
        for i in x:
            sum +=i

       #option1 tc O(N)
        for i in range(len(x)):
            r= sum-x[i]-l
            if l==r:
                return i
            l+=x[i]
            print(l,r)
        return -1

        #alternative TC=O(N)
        for i in range(len(x)):
            sum-=x[i]
            r=sum
            if l==r:
                return i
            l+=x[i]
        return -1
riki= Ri()
print(riki.ri([1,3]))   