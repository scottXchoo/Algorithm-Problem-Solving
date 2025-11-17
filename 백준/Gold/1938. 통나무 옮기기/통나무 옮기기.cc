#include <iostream>
#include <queue>

#define MAX 55
using namespace std;

int N, B_shape, E_shape;
char maps[MAX][MAX];
int visited[MAX][MAX][2];

pair<int, int> Start[3], End[3], B_center, E_center;

// 순서: 반시계 방향으로 회전
int c_dx[8] = {-1, 0, 1, 1, 1, 0, -1, -1};
int c_dy[8] = {-1, -1, -1, 0, 1, 1, 1, 0};

void input() {
    int s_idx = 0;
    int e_idx = 0;
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> maps[i][j];
            if (maps[i][j] == 'B') {
                // 통나무 첫 위치를 Start 배열로 관리
                Start[s_idx].first = i;
                Start[s_idx].second = j;
                s_idx++;

                maps[i][j] = '0';
            } else if (maps[i][j] == 'E') {
                // 최종 위치를 End 배열로 관리
                End[e_idx].first = i;
                End[e_idx].second = j;
                e_idx++;

                maps[i][j] = '0';
            }
        }
    }
    // B와 E의 중심점을 따로 관리
    B_center.first = Start[1].first;
    B_center.second = Start[1].second;
    E_center.first = End[1].first;
    E_center.second = End[1].second;
}

// 가로인지 세로인지 확인: 가로 = 0 & 세로 = 1
int check_shape(pair<int, int> s[3]) {
    if (s[0].first == s[1].first && s[1].first == s[2].first) return 0; // 가로형
    return 1; // 세로형
}

// 돌릴 수 있는지 확인: 돌릴 수 있음 = 1 & 돌릴 수 없음 = 0
int change_shape(int x, int y, int shape) {
    if (shape == 0) { // 가로형
        for (int i = 0; i < 8; i++) {
            if (i == 1 || i == 5) continue; // 가로형이기에 (0, -1), (0, 1)은 신경 X

            int nx = x + c_dx[i];
            int ny = y + c_dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N) return 0;
            if (maps[nx][ny] == '1') return 0;
        }
    } else { // 세로형
        for (int i = 0; i < 8; i++) {
            if (i == 3 || i == 7) continue; // 세로형이기에 (1, 0), (-1, 0)은 신경 X

            int nx = x + c_dx[i];
            int ny = y + c_dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N) return 0;
            if (maps[nx][ny] == '1') return 0;
        }
    }
    return 1;
}

int bfs() {
    queue<pair<pair<int, int>, pair<int, int>>> q;
    // queue: (B의 중심점 x, y), (B의 방향, count)
    int b_x = B_center.first;
    int b_y = B_center.second;
    q.push(make_pair(make_pair(b_x, b_y), make_pair(B_shape, 0)));
    visited[b_x][b_y][B_shape] = 1;

    while (!q.empty()) {
        int x = q.front().first.first;
        int y = q.front().first.second;
        int s = q.front().second.first;
        int cnt = q.front().second.second;
        q.pop();

        // E의 중심점이 B의 중심점과 같고 && 방향까지 같다면 => 그때가 정답
        if (x == E_center.first && y == E_center.second && s == E_shape) {
            return cnt;
        }

        if (s == 0) { // BBB가 가로형
            // Up
            int nx = x - 1;
            int ny = y;
            if (!(nx < 0 || ny - 1 < 0 || ny + 1 >= N || visited[nx][ny][s])) {
                if (maps[nx][ny] == '0' && maps[nx][ny - 1] == '0' && maps[nx][ny + 1] == '0') {
                    q.push(make_pair(make_pair(nx, ny), make_pair(s, cnt + 1)));
                    visited[nx][ny][s] = 1;
                }
            }

            // Down
            nx = x + 1;
            ny = y;
            if (!(nx < 0 || ny - 1 < 0 || ny + 1 >= N || visited[nx][ny][s])) {
                if (maps[nx][ny] == '0' && maps[nx][ny - 1] == '0' && maps[nx][ny + 1] == '0') {
                    q.push(make_pair(make_pair(nx, ny), make_pair(s, cnt + 1)));
                    visited[nx][ny][s] = 1;
                }
            }

            // Left
            nx = x;
            ny = y - 1;
            int nny = y - 2; // 맨 끝 확인 필요
            if (!(nny < 0 || visited[nx][ny][s])) {
                if (maps[nx][nny] == '0') {
                    q.push(make_pair(make_pair(nx, ny), make_pair(s, cnt + 1)));
                    visited[nx][ny][s] = 1;
                }
            }

            // Right
            nx = x;
            ny = y + 1;
            nny = y + 2;
            if (!(nny >= N || visited[nx][ny][s])) {
                if (maps[nx][nny] == '0') {
                    q.push(make_pair(make_pair(nx, ny), make_pair(s, cnt + 1)));
                    visited[nx][ny][s] = 1;
                }
            }

            // Turn
            if (change_shape(x, y, s) == 1 && visited[x][y][1] == 0) { // 세로형으로 바꿀 수 있고 & 세로형 중심 방문 X
                // 중심 (x, y)는 그대로 && 방향만 1로 변경
                q.push(make_pair(make_pair(x, y), make_pair(1, cnt + 1)));
                visited[x][y][1] = 1;
            }
        } else { // BBB가 세로형
            // Up
            int nx = x - 1;
            int ny = y;
            int nnx = x - 2;
            if (!(nnx < 0 || visited[nx][ny][s])) {
                if (maps[nnx][ny] == '0') {
                    q.push(make_pair(make_pair(nx, ny), make_pair(s, cnt + 1)));
                    visited[nx][ny][s] = 1;
                }
            }

            // Down
            nx = x + 1;
            ny = y;
            nnx = x + 2;
            if (!(nnx >= N || visited[nx][ny][s])) {
                if (maps[nnx][ny] == '0') {
                    q.push(make_pair(make_pair(nx, ny), make_pair(s, cnt + 1)));
                    visited[nx][ny][s] = 1;
                }
            }

            // Left
            nx = x;
            ny = y - 1;
            if (!(ny < 0 || nx - 1 < 0 || nx + 1 >= N || visited[nx][ny][s])) {
                if (maps[nx][ny] == '0' && maps[nx - 1][ny] == '0' && maps[nx + 1][ny] == '0') {
                    q.push(make_pair(make_pair(nx, ny), make_pair(s, cnt + 1)));
                    visited[nx][ny][s] = 1;
                }
            }

            // Right
            nx = x;
            ny = y + 1;
            if (!(ny >= N || nx - 1 < 0 || nx + 1 >= N || visited[nx][ny][s])) {
                if (maps[nx][ny] == '0' && maps[nx - 1][ny] == '0' && maps[nx + 1][ny] == '0') {
                    q.push(make_pair(make_pair(nx, ny), make_pair(s, cnt + 1)));
                    visited[nx][ny][s] = 1;
                }
            }

            // Turn
            if (change_shape(x, y, s) == 1 && visited[x][y][0] == 0) { // 가로형으로 바꿀 수 있고 & 가로형 중심 방문 X
                q.push(make_pair(make_pair(x, y), make_pair(0, cnt + 1)));
                visited[x][y][0] = 1;
            }
        }
    }
    return 0;
}

int main() {
    input();

    B_shape = check_shape(Start);
    E_shape = check_shape(End);

    int answer = bfs();
    cout << answer << '\n';

    return 0;
}