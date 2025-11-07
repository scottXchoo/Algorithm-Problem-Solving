#include <iostream>
#include <queue>
#include <tuple>
#include <cstring>

using namespace std;

#define MAX 205

int K, W, H;
int maps[MAX][MAX]{};
int visited[MAX][MAX][35]{};

int dx[12] = { 0,0,1,-1,-2,-2,-1,-1,1,1,2,2 };
int dy[12] = { 1,-1,0,0,-1,1,-2,2,-2,2,-1,1 };
int answer = 1e9;
bool flag = false;

void input() {
    cin >> K >> W >> H;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> maps[i][j];
        }
    }
}

void bfs() {
    queue<tuple<int, int, int, int>> q;
    q.push({0, 0, 0, 0}); // x, y, 이동 횟수, 말 점프 카운트

    while (!q.empty()) {
        int cx = get<0>(q.front());
        int cy = get<1>(q.front());
        int dist = get<2>(q.front());
        int k_cnt = get<3>(q.front());
        q.pop();

        // 최종 지점에 도착해야 answer = dist로 업데이트
        // 즉, 최종 지점에 도착하지 못하면, answer는 그대로 -1임
        if (cx == H - 1 && cy == W - 1) {
            answer = answer < dist ? answer : dist;
            flag = true;
        }

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (nx < 0 || nx >= H || ny < 0 || ny >= W || visited[nx][ny][k_cnt]) continue;
            if (maps[nx][ny]) continue;

            visited[nx][ny][k_cnt]++;
            q.push({nx, ny, dist + 1, k_cnt});
        }
        if (k_cnt < K) { // 말 점프 사용 가능할 때
            for (int i = 4; i < 12; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx < 0 || nx >= H || ny < 0 || ny >= W || visited[nx][ny][k_cnt + 1]) continue;
                if (maps[nx][ny]) continue;

                visited[nx][ny][k_cnt + 1]++;
                q.push({nx, ny, dist + 1, k_cnt + 1}); // 말 점프 카운트 + 1
            }
        }
    }
}

int main() {
    input();

    bfs();

    if (!flag) {
        cout << -1;
    } else {
        cout << answer;
    }

    return 0;
}