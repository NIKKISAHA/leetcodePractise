class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        o=[]
        for i in range(2):
            for j in nums:
                o.append(j)
        return o