from collections import defaultdict
class Ri():
    def ri(self,x:list[int])->int:
        x.sort()
        return x[len(x)//2]

        # anather solution using hashmap
        h=defaultdict(int)
        print(h)
        for i in x:
            h[i]+=1
        n=len(x)//2
        for key,value in h.items():
            if value>n:
                return key
            
        #anather solution see nc on yt
        res,count=0,0
        for i in x:
            if count==0:
                res=i
            count+=(1 if res==i else -1)
        return res

    
riki= Ri()
print(riki.ri([3,2,3,5,5,5,5])) 