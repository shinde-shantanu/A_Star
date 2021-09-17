import timeit

def dist(i, j, dim, heu):
    if heu == 1:
        return ( ((i-dim-1) ** 2) + ((j-dim-1) ** 2) ) ** 0.5
    if heu == 2:
        return abs(dim-1-i)+abs(dim-1-j)
    if heu == 3:
        return max(abs(i-dim-1),abs(j-dim-1))

def insert_fringe(i, j, fringe, f):
    #print(fringe)
    if len(fringe)==0:
        fringe.append((i,j))
    else:
        for x in range(len(fringe)):
            (I,J)=fringe[x]
            if f[I][J]<f[i][j]:
                fringe.insert(x, (i,j))
                return
        fringe.append((i,j))

def a_star(dim, P, grid, heu):
    
    start=timeit.default_timer()
    
    result=False
    
    g=[[-1 for i in range(dim)] for j in range(dim)]
    g[0][0]=0
    
    h=[[dist(i,j,dim,heu) for i in range(dim)] for j in range(dim)]

    f=[[-1 for i in range(dim)] for j in range(dim)]
    f[0][0]=g[0][0]+h[0][0]
    p=[[-1 for i in range(dim)] for j in range(dim)]
    p[0][0]=0
    
    fringe=[(0,0)]
    
    while len(fringe)!=0:
        (i,j)=fringe.pop(0)
        if (i,j) == (dim-1,dim-1):
            result=True
            break
        #print((i,j))
        if i-1 >= 0 and grid[i-1][j] != 1 and p[i-1][j]==-1 and p[i][j] != (i-1,j):
            p[i-1][j]=(i,j)
            g[i-1][j]=g[i][j]+1
            f[i-1][j]=g[i-1][j]+h[i-1][j]
            insert_fringe(i-1,j,fringe,f)
            
        if j+1 < dim and grid[i][j+1] != 1 and p[i][j+1]==-1 and p[i][j] != (i,j+1):
            p[i][j+1]=(i,j)
            g[i][j+1]=g[i][j]+1
            f[i][j+1]=g[i][j+1]+h[i][j+1]
            insert_fringe(i,j+1,fringe,f)
            
        if i+1 < dim and grid[i+1][j] != 1 and p[i+1][j]==-1 and p[i][j] != (i+1,j):
            p[i+1][j]=(i,j)
            g[i+1][j]=g[i][j]+1
            f[i+1][j]=g[i+1][j]+h[i+1][j]
            insert_fringe(i+1,j,fringe,f)
            
        if j-1 >= 0 and grid[i][j-1] != 1 and p[i][j-1]==-1 and p[i][j] != (i,j-1):
            p[i][j-1]=(i,j)
            g[i][j-1]=g[i][j]+1
            f[i][j-1]=g[i][j-1]+h[i][j-1]
            insert_fringe(i,j-1,fringe,f)
    
    stop=timeit.default_timer()

    #for x in p:
        #print(x)

    #print("Time: ", stop-start)
    #print(start)
    #print(stop)

    return(result, start, stop, p)


##dim=101
##P=0.25
##grid=gen_grid(dim,p)
##
##print("Grid:")
##for x in grid:
##    print(x)
##
##result, start, stop, p = a_star(dim, P, grid, 1)
##
##for x in p:
##    print(x)
##print("Time: ", stop-start)
##print(result)
