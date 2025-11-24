#include <iostream>
#include <queue>
#include <cstring>
#include <tuple>
#define MAX 1005
using namespace std;

int N, M, K;
int maps[MAX][MAX];
queue<tuple<int, int, int, int>> q; // x, y, cnt, wall
int visited[MAX][MAX][15];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};

void input() {
    cin >> N >> M >> K;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            char input = '0';
            cin >> input;
            maps[i][j] = input - '0';
        }
    }
}

int bfs() {
    q.push({1, 1, 1, 0});
    visited[1][1][0] = 1;

    while (!q.empty()) {
        int cx = get<0>(q.front());
        int cy = get<1>(q.front());
        int cnt = get<2>(q.front());
        int wall = get<3>(q.front());
        q.pop();

        if (cx == N && cy == M) {
            return cnt;
        }

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (nx <= 0 || nx > N || ny <= 0 || ny > M) continue;

            int next_wall = wall + 1;
            // 다음 칸 0이고 방문하지 않았다면
            if (maps[nx][ny] == 0 && !visited[nx][ny][wall]) {
                q.push({nx, ny, cnt + 1, wall});
                visited[nx][ny][wall] = 1;
            } else if (maps[nx][ny] == 1 && !visited[nx][ny][next_wall]) { // 다음 칸 1인데, 벽 부술 수 있다면
                if (next_wall == K + 1) continue; // K까지는 가능
                
                q.push({nx, ny, cnt + 1, next_wall});
                visited[nx][ny][next_wall] = 1;
            }
        }
    }
    return -1;
}

int main() {
    input();

    int answer = bfs();
    cout << answer;

    return 0;
}