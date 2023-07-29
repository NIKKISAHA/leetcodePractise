#find dissapeared number from a range , ex ->[1,2,4] -> 3
class Ri():
    def ri(self, x:list[int])->list[int]:
        newarray=[]
        maxx=0
        for i in x:
            maxx=max(maxx,i)
        for i in range(1,maxx+1):
            if i not in set(x):
                newarray.append(i)
        return newarray

        #anather if one element
        # summ=0
        # maxx=0
        # for i in x:
        #     maxx=max(maxx,i)
        # print(maxx)
        # for i in range(1,maxx+1):
        #     summ+=i
        # print (summ ,sum(set(x)))
        # return summ - sum(set(x))
       
riki= Ri()
print(riki.ri([1,8,10,10])) 