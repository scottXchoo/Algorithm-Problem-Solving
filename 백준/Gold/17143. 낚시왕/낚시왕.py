from copy import deepcopy
R,C,M=map(int,input().split())

graph=[[[]for _ in range(C)] for _ in range(R)]

dx=[-1,1,0,0]
dy=[0,0,1,-1]

for _ in range(M):
    x,y,s,d,z=map(int,input().split())
    x-=1
    y-=1
    d-=1
    graph[x][y]=[s,d,z]

answer=0
for king in range(C):
    #왕이 물고기를 먹어줌
    now=0
    while now<R:
        if graph[now][king]:
            answer+=graph[now][king][2]
            graph[now][king]=[]
            break
        now+=1
    temp=[[[]for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if graph[x][y]:
                s,d,z=graph[x][y]
                #위 아래로 움직이는 경우
                if d==0 or d==1:
                    s=s%(2*(R-1))
                #좌우로 움직이는 경우
                elif d==2 or d==3:
                    s=s%(2*(C-1))
                nx=x
                ny=y
                move=0
                while move<s:
                    nx+=dx[d]
                    ny+=dy[d]
                    if nx<0 or nx>=R or ny<0 or ny>=C:
                        nx-=dx[d]
                        ny-=dy[d]
                        if d==0: d=1
                        elif d==1 :d=0
                        elif d==2 :d=3
                        elif d==3:d=2

                    else:
                        move+=1
                #이동한 곳에 상어가 있을 경우
                if temp[nx][ny]:
                    n_size=z
                    go_size=temp[nx][ny][2]
                    #지금 움직이는 상어가 더 크다면, 지금 상어로 최신화(큰 걸로 먹는다는 개념)
                    if n_size>go_size:
                        temp[nx][ny]=[s,d,z]

                else:
                    temp[nx][ny]=[s,d,z]

    graph=deepcopy(temp)

print(answer)