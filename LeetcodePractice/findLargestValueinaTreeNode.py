#find largest value in a tree row
class node():
    def __init__(self,val,left=None,right=None) -> None:
        self.val=val
        self.right=right
        self.left=left
from collections import deque
def ri(root:node)->list[int]:
        newarr=[]
        arr = deque([root])
        while arr:
             max_num=arr[0].val
             for _ in range(len(arr)):
                root = arr.popleft()
                max_num=max(root.val,max_num)
                if root.left:arr.append(root.left)
                if root.right:arr.append(root.right)
             newarr.append(max_num)
        return newarr
a=node(10)
b=node(20)
c=node(30)
d=node(40)
e=node(50)
f=node(60)
a.left=b
a.right=c
b.left=d
b.right=e
c.right=f

print(ri(a))                  
             