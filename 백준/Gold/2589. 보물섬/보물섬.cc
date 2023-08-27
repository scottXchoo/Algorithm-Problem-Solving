#include <bits/stdc++.h>
using namespace std;
int m, n, visited[54][54], mx;
const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};
char a[54][54];

void bfs(int y, int x) {
    // bfs 초기화
    memset(visited, 0, sizeof(visited));
    visited[y][x] = 1;
    // y, x를 담는 이차원 배열이기 때문에 pair<int, int>
    queue<pair<int, int>> q;
    q.push({y, x});
    while(q.size()) {
        tie(y, x) = q.front(); q.pop();
        for(int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if(ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
            if(visited[ny][nx]) continue;
            if(a[ny][nx] == 'W') continue;
            visited[ny][nx] = visited[y][x] + 1;
            q.push({ny, nx});
            mx = max(mx, visited[ny][nx]);
        }
    }
}

int main() {
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(a[i][j] == 'L') bfs(i, j);
        }
    }
    cout << mx - 1 << '\n';
}