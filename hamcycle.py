def mprint(par,last):
    c=last
    while(c!= -1):
        print(c,"->",end="")
        c=par[c]
    
def hcycle(n,graph,par,visited,l,cur):
    if(n==1):
        return True
    if(l==1):
        if(graph[cur][0] or graph[0][cur]):
            mprint(par,cur)
            return True
        else:
            return False
    for i in range(n):
        if( (graph[cur][i] or graph[i][cur]) and (not visited[i]) ):
            visited[i]=True
            par[i]=cur
            if(hcycle(n,graph,par,visited,l-1,i) ):
                return True
            visited[i]=False
            par[i]=-1
    return False

if(__name__=="__main__"):
    n=5
    g=[[False for i in range(n)] for j in range(n)]
    g[0][1],g[0][3]=True,True
    g[1][2],g[1][3],g[1][4]=True,True,True
    g[2][4]=True
    g[3][4]=True
    par=[-1 for i in range(n)]
    v=[False for i in range(n)]
    v[0]=True
    if( hcycle(n,g,par,v,n,0) ):
        print("HamCycle Exists")
    else:
        
        print("HamCycle does not Exists")
    
