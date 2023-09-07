#car parking
class Ri():
    def __init__(self,large:int,small:int,medium:int) -> None:
        self.li=[large,small,medium]
    def ri(self,num:int)->bool:
        if self.li[num-1] > 0:
            self.li[num-1] -=1
            return True
        return False
riki = Ri(1,2,1)
print(riki.ri(2))
print(riki.ri(2))
print(riki.ri(2))
print(riki.ri(1))