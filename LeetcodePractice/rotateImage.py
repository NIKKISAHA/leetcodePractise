#rotate image 
class Ri():
    def ri(self,x:list[list[int]])->list[list[int]]:
        #leetcode
        # print(x[::-1])
        # x[:]=zip(*x[::-1])
        x[:]=map(list,zip(*x[::-1]))
        return x
    
        #reverse then transpose 
        #reverse [[1,2,3],[4,5,6],[7,8,9]] -> [[7,8,9],[4,5,6],[1,2,3]]
        l,r=0,len(x)-1
        while l<r:
            x[l],x[r]=x[r],x[l]
            l+=1
            r-=1
        #or x[:]=x[::-1] for reverse 
        #transpose [[7,8,9],[4,5,6],[1,2,3]]->[[7, 4, 1], [8, 5, 2], [9, 6, 3]] row becomes col ,col becomes row
        for i in range(len(x)):
            for j in range(i):
                x[i][j],x[j][i]=x[j][i],x[i][j]
                print(x[i][j],x[j][i],x[j][i],x[i][j])
        return x
riki = Ri()
print(riki.ri([[1,2,3],[4,5,6],[7,8,9]]))
# print(riki.ri([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))

