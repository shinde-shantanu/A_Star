import random

def gen_grid(dim, p):

    s=[]
    for i in range(dim):
        for j in range(dim):
            if (i,j) == (0,0) or (i,j) == (dim-1,dim-1):
                continue
            else:
                s.append((i,j))
    
    k=int(p*((dim*dim)-2))
    blocked=random.sample(s,k)
    
    grid=[[0 for i in range(dim)] for j in range(dim)]

    for x in blocked:
        grid[x[0]][x[1]]=1

    return grid
