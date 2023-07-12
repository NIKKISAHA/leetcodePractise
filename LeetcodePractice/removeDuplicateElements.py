#remove duplicate elements ex:[0,0,1,3,3]->[0,1,3,3,3]
class Ri():
    def ri(self,x:list[int])->int:
        change=1
        for i in range(1,len(x)):
            if x[i]!=x[i-1]:
                x[change]=x[i]
                change+=1
        return change # , x
riki= Ri()
print(riki.ri([0,0,1,3,3,5,7,7,8]))

#anather solution of previus using set
def ri(x):
    x[:]=sorted(set(x)) #when we use x[:]==sorted(set(x)) it does in place but in x=sorted(set(x)) it creates anather array
    return len(x) , x
print(ri([0,0,1,3,3,5,7,7,8]))

# anather solution
def ri(x:int)->int:
    i=1
    while i<len(x):
        if x[i]==x[i-1]:
            x.pop(i)
        else:
            i+=1
    return len(x)
print(ri([0,0,1,3,3,5,7,7,8]))