#include <bits/stdc++.h>
using namespace std;

const int max_n = 104;
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
int n, m, a[max_n][max_n], visited[max_n][max_n], y, x;

int main() {
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            scanf("%1d", &a[i][j]);
        }
    }
    
    queue<pair<int, int>> q;
    visited[0][0] = 1;
    q.push({0, 0});
    while(q.size()) {
        // y, x를 뽑아내기
        tie(y, x) = q.front(); q.pop();
        for(int i = 0; i < 4; i++) {
            // 4방향 탐색
            int ny = y + dy[i];
            int nx = x + dx[i];
            // 오버 & 언더 플로 방지
            if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
            // 0은 이동할 수 없는 칸
            if(a[ny][nx] == 0) continue;
            // 방문한 곳은 지나가기
            if(visited[ny][nx]) continue;
            // 방문한 횟수 누적합 = 최단경로 횟수
            visited[ny][nx] = visited[y][x] + 1;
            q.push({ny, nx});
        }
    }
    printf("%d", visited[n - 1][m - 1]);
    return 0;
}