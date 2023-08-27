#happy number
class Ri():
    def ri(self,x:int)->bool:
        h=set()
        while x not in h:
            h.add(x)
            if x==1:
                return True
            x=sum([(int(i))**2 for i in str(x)]) #x=self.func(x) #define func later
        return False
    #for anather solution
#     def func(self,x:int)->int:
#         s=0
#         while x:
#             p= x%10
#             p=p**2
#             s+=p
#             x//=10
#         return 

       #new solution
#       def ri(self,x:int,visited=None)->bool:
#         if visited is None:
#            visited=set()
#         if x==1:
#            return True
#         if x in visited:
#            return False
#         visited.add(x)
#         x=sum([(int(i))**2 for i in str(x)])
#         return self.ri(x,visited)
riki = Ri()
print(riki.ri(20))