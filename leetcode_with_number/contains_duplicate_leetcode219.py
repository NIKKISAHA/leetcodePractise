class Ri():
    def ri(self,nums:list[int],k:int)->bool:
        o = set()
        l=0
        for i in range(len(nums)):
            if i - l > k:
                o.remove(nums[l])
                l+=1
            if nums[i] in o:
                return True
            o.add(nums[i])
        return False
    
riki = Ri()
print(riki.ri([1,2,3,1],1))