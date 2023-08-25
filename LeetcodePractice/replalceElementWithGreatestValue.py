#replace element with the greatest value and last one = -1; ex:[7,1,2]->[2,2,-1]
#replace with the greatest element of right , [8,2,1]->[2,1,-1]
class Ri():
    def ri(self,x:list[int])->list[int]:
        # rightMost=-1
        # for i in range(len(x)-1,-1,-1):
        #    temp = max(rightMost,x[i])
        #    x[i]=rightMost
        #    rightMost=temp
        #    print(rightMost)
        # return x

        #anather one
        # x[:],maxi=x[::-1],-1
        # for i in range(len(x)):
        #     x[i],maxi=maxi,max(maxi,x[i])
        # return x[::-1]
    
        #anather one
        mx=-1
        for i in range(len(x)-1,-1,-1): #range(len(x)-1,-1,-1) is for trivas through in reverse order
            x[i] ,mx=mx,max(x[i],mx) #x[i] will always be equal to mx and new mx will be the max of (x[i] or previous mx)
            # print(x[i]) #for i in x expression i = the number, but for range function i = index
        return x
riki = Ri()
print(riki.ri([8,2,1]))
