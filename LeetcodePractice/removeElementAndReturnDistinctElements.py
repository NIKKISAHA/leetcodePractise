#remove elements from an array ex: arr= [1,2,2,3,3],remove 2 -> [1,3,3,_,_],3 unique items
class Ri():
    def ri(self,x:list[int],tar:int)->int:
        # f=0
        # for i in x:
        #     if i != tar:
        #         x[f]=i
        #         f+=1


        # or

        # for i in range(len(x))[::-1]:
        #     if x[i] != tar:
        #         x[f]=x[i]
        #         f+=1

        # or
        x[:]=[i for i in x if i != tar]

        return len(x)
riki= Ri()
print(riki.ri([1,2,2,3],2))

#rough
n=[1,2,2,3]
print(range(len(n))[::-1])

