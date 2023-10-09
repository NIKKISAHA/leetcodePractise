#minimum path sum 
class Ri():
    def ri(self,x:list[list[int]])->int:
        rows,cols=len(x),len(x[0])
        res=[[float("inf")]*(cols+1) for i in range(rows+1)]
        res[rows-1][cols]=0
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                res[i][j]=x[i][j]+min(res[i+1][j],res[i][j+1])
        return res[0][0]
riki=Ri()
print(riki.ri([[1,3,1],[1,5,1],[4,2,1]]))