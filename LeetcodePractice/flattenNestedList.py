# #flatten nested list
class Ri():
    def __init__(self) -> None:
        self.new=[]
        
    def ri(self,x)->list[int]:

        for i in range(len(x)):
                #isinstance checks if the variable is a certain data type , it takes two argument, (variable,type)
                if isinstance(x[i],int):
                        self.new.append(x[i])
                else:
                        self.ri(x[i])
        return self.new

riki=Ri()
print(riki.ri([2,4,[2,4,[1,[0,9]]]]))