#coins fit 
class Ri():
    def ri(self,x:int)->int:
#         #solution o(n)
        m=1
        r=0
        for i in range(1,x+1):
                x= x-i
                # print(x)
                if x<0:
                        return r
                r+=1
        return r
        
#         #log(n)
        l,r=0,x
        while l <=r:
            mid= (l+r)//2
            t=mid *(mid+1)//2 #(mid/2)*(mid+1)
            if t==x:
                return mid
            if t>x:
                r=mid-1
            else:
                l=mid+1
        return r

#         # o(n)\
        r,s=1,1
        while s<=x:
                s=s+r+1
                print(s)
                r+=1
                print(r)
        return r-1
riki= Ri()
print(riki.ri(7)) 
# # 1
# # 23
# # 456
# #7,8,9,10

