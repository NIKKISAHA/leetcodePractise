#ugly number aka numbers who are fully divisible by 2,3,5
class Ri():
    def ri(self,x:int)->bool:
        #solution 1 using while loop , TC=O(logn)
        while x%2==0:
            x=x//2
        while x%3==0:
            x=x//3 
        while x%5==0:
            x=x//5
        if(x==1):
            return True
        return False

        #solution 2 using for loop , TC=O(logn)
        for i in [2,3,5]:
                if x%i==0:
                     x=x//i
        return x==1
riki= Ri()
print(riki.ri(2))