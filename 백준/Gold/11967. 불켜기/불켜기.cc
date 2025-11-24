#include <iostream>
#include <map>
#include <queue>
#define MAX 105
using namespace std;

int N, M;
int rooms[MAX][MAX];
vector<pair<int, int>> adj[MAX][MAX];
int visited[MAX][MAX];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int answer;

void input() {
    cin >> N >> M;
    for (int j = 0; j < M; j++) {
        int x_1, y_1, x_2, y_2;
        cin >> x_1 >> y_1 >> x_2 >> y_2;
        adj[x_1][y_1].push_back({x_2, y_2});
    }
}

int bfs() {
    queue<tuple<int, int>> q; // x, y
    q.push({1, 1});
    visited[1][1] = 2;

    int cnt = 1;
    while (!q.empty()) {
        int cx = get<0>(q.front());
        int cy = get<1>(q.front());
        q.pop();

        // cout << "cx: " << cx << ", " << "cy: " << cy << "\n";

        // 불 킬 수 있는 곳 다 켜기
        for (auto p : adj[cx][cy]) {
            int nx = p.first, ny = p.second;
            // 1이거나 2는 다 continue
            if (visited[nx][ny]) continue;

            // 불 켰다고 알려주기 + cnt 증가
            visited[nx][ny] = 1;
            cnt++;

            // 불을 킨 곳 주변 탐색
            for (int i = 0; i < 4; i++) {
                int nnx = nx + dx[i];
                int nny = ny + dy[i];
                // 주변에 불 킨 곳이 있네? 거기부터 다시 탐색 고고
                if (visited[nnx][nny] == 2) {
                    q.push({nnx, nny});
                    break; // 여기서 왜 break?
                }
            }
        }

        // 주변에 불 켜진 곳이 있으면, 탐색 고고
        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            if (visited[nx][ny] == 1) {
                visited[nx][ny] = 2;
                q.push({nx, ny});
            }
        }
    }

    return cnt;
}

int main() {
    input();

    answer = bfs();
    cout << answer << "\n";

    return 0;
}