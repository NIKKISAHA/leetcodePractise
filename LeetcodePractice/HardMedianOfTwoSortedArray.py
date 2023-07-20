# # median of two sorted array - hard , tc=O(log(m+n)) youtube neetcode
# class Ri():
#     def ri(self,x:list[int],y:list[int])->float:
#         total=len(x)+len(y)
#         half=total//2
        
#         a=x
#         b=y
#         if len(x)>len(y):
#             a,b=b,a
        
#         l,r=0,len(a)-1
#         while True:
#            i =( l+r )//2
#            j= half - i -2

#            aleft=a[i] if i>=0 else float("-infinity")
#            aright=a[i+1] if (i+1)<len(a) else float("infinity")
#            bleft=b[j] if j>=0 else float("-infinity")
#            bright=b[j+1] if (j+1)<len(b) else float("infinity")

#            if aleft<= bright and aright>= bleft:
#                if total%2:
#                    return float(min(aright,bright))
#                else:
#                    return float((min(aright,bright) + max(aleft,bleft))/2)
#            elif aleft>bright:
#                r=i-1
#            else:
#                l=i+1

# riki= Ri()
# print(riki.ri([1,2,3,9,11],[2,4,5,5,5,6,9,11]))# 122345556911

# class Solution:  # Time: O(log(min(m, n))) and Space: O(n) leetcode guy solution
#     def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
#         A, B = nums1, nums2
#         total = len(nums1) + len(nums2)
#         half = total // 2

#         if len(A) > len(B):    # for our solution we are assuming that B will be bigger than A, if it's not given than make it
#             A, B = B, A

#         l, r = 0, len(A) - 1   # we also assume that A is exactly half of B

#         while True:            # when any return statement is executed it will stop
#             i = (l + r) // 2   # A[mid]

#             # B[mid] = total//2(divide by 2 will get us mid B ) - A[mid](if we sub A from total, B's left) -
#             # 2(to make it align with starting index 0 of A & B, else it will go out of bounds)
#             j = half - i - 2

#             Aleft = A[i] if i >= 0 else float("-infinity")  # if index i is in negative than assign -infinity to Aleft
#             Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")  # if index i+1 is greater than the size of A assign infinity to Aright
#             Bleft = B[j] if j >= 0 else float("-infinity")  # if index j is in negative than assign -infinity to Bleft
#             Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")  # if index j+1 is greater than the size of B assign infinity to Bright

#             # A = [1, 2, 3(left), 4(right), 5] and B = [1, 2, 3(left), 4(right), 5, 6, 7, 8]  # B = 6 - 2 - 2 = 2(i.e 0,1,2)
#             if Aleft <= Bright and Bleft <= Aright:  # 3 <= 4 and 3 <= 4
#                 if total % 2:                                         # odd: min(4, 4)
#                     return min(Aright, Bright) 
#                 return (max(Aleft, Bleft) + min(Aright, Bright)) / 2  # even: max(3, 3) + min(4, 4)  / 2
#             elif Aleft > Bright:  # A = [1, 2, 3(left), 4(right), 5, 6] and B = [1, 2(left), 3(right), 4, 5]
#                 r = i - 1         # r = 3 - 1 = 2(i.e. index 0,1,2) --> A = [1, 2(L), 3(R), 4, 5, 6] and B = [1, 2, 3(L), 4(R), 5, 6]
#             else:                 # when Bleft > Aright, we will increase l so L becomes R, and R pointer is shifted to R+1 index
#                 l = i + 1
# riki= Solution()
# print(riki.findMedianSortedArrays([1,2,3,9,11],[2,4,5,5,5,6,9,11,33,34,34]))

#leetcode editorial solution
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)


        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            maxLeftA = float('-inf') if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float('inf') if partitionA == m else nums1[partitionA]
            maxLeftB = float('-inf') if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float('inf') if partitionB == n else nums2[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1

riki= Solution()
print(riki.findMedianSortedArrays([1,2,3,9,11],[2,4,5,5,5,6,9,11,33,34,34]))