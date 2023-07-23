import heapq
class Ri():
    def __init__(self,k:int,x:list[int]) -> None:
        self.minheap,self.k = x , k
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

    def add(self, j:int)->int:
        heapq.heappush(self.minheap,j)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
    
riki= Ri(3,[5,7,8,9])
print(riki.add(8)) 

# anather solution (simple without the add function) both solution tc=o(nlog)
def ri(k:int,x:list[int])->int:
    heap=[]
    for i in x:
        heapq.heappush(heap,i)
        if len(heap)>k:
            heapq.heappop(heap)
    return heap[0]

    # alternative 
    x.sort(reverse=True)
    print(x)
    return x[k-1]
print(ri(3,[5,7,8,9]))
