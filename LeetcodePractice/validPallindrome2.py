#valid palindrome 2
class Ri():
    def ri(self,x:str)->bool:
        l,r=0,len(x)-1
        while l<r:
            if x[l]!=x[r]:
                left ,right = x[l+1:r+1],x[l:r]
                return ((left == left[::-1]) or (right == right[::-1]))
            l,r=l+1,r-1
        return True
        
        #anather solution
        def varify(x:str,l:str,r:str,deleted:bool)->bool:
            if len(x)<3:return True
            while l<r:
                if x[l]!=x[r]:
                    if deleted:
                        return False
                    else:
                        return varify(x,l+1,r,True) or varify(x,l,r-1,True)
                else:
                    l,r=l+1,r-1
                return True
        return varify(x,0,len(x)-1,False)
                       
riki = Ri()
print(riki.ri("hxo"))