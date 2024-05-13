class Ri:
    def ri(self,nums:list[int],k:int)->int:
        j=0
        for i in range(len(nums)):
            if nums[i] != k:
                nums[j]=nums[i]
                j+=1
        return j
riki = Ri()    
print(riki.ri([1,2,3,2,4,6,2,9],2))

