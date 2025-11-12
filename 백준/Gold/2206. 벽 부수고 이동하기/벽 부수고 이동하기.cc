#include <iostream>
#include <queue>
#include <tuple>

#define MAX 1005

using namespace std;

int N, M;
int maps[MAX][MAX]{};
int visited[MAX][MAX][5]{};
int dx[5] = {0, 0, 1, -1};
int dy[5] = {1, -1, 0, 0};
int flag = 0;
int answer = 1e9;

void input() {
    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        char inputs;
        for (int j = 1; j <= M; j++) {
            cin >> inputs;
            int temp = inputs - '0';
            maps[i][j] = temp;
        }
    }
}

void bfs() {
    queue<tuple<int, int, int, int>> q;
    q.push({1, 1, 1, 0}); // x, y, 거리, 벽 뚫은 여부
    visited[1][1][0] = 1;

    while (!q.empty()) {
        int cx = get<0>(q.front());
        int cy = get<1>(q.front());
        int dist = get<2>(q.front());
        int wall = get<3>(q.front());
        q.pop();

        if (cx == N && cy == M) {
            answer = min(answer, dist);
            flag = 1;
            continue; // 도달하면, 더 진행할 필요 없잖아?
        }

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            // 범위 나가면, 건너뛰기
            if (nx <= 0 || nx >= N+1 || ny <= 0 || ny >= M+1) continue;

            if (wall == 0 && maps[nx][ny] == 1) {
                q.push({nx, ny, dist + 1, wall + 1});
                visited[nx][ny][wall + 1] = 1;
            } else if (!visited[nx][ny][wall] && !maps[nx][ny]) {
                q.push({nx, ny, dist + 1, wall});
                visited[nx][ny][wall] = 1;
            }
        }
    }
}

int main() {
    input();

    bfs();

    if (flag) {
        cout << answer;
    } else {
        cout << -1;
    }

    return 0;
}