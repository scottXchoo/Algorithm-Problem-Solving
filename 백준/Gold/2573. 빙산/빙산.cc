#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

#define MAX 300

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int N, M;
int maps[MAX][MAX];
int upd_maps[MAX][MAX];
int visited[MAX][MAX];
int answer = 0; // 빙산이 두 덩어리가 될 때까지 걸린 시간
int iceberg_cnt = 0; // 빙산의 개수 (빙산이 다 녹으면, 끝)
int dung_cnt = 0; // 덩어리 개수 (덩어리 개수에 따라 끝날 수 있음)
queue<pair<int, int>> q;

void input() {
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> maps[i][j];
            upd_maps[i][j] = maps[i][j];
        }
    }
}

void copy_map() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            maps[i][j] = upd_maps[i][j];
        }
    }
}

void melt_iceberg() {
    iceberg_cnt = 0; // 초기화 필요

    // (1, 1)부터 (N-2, M-2)까지 for문
    for (int x = 1; x < N - 1; x++) {
        for (int y = 1; y < M - 1; y++) {
            if (maps[x][y] > 0) { // 바다가 아니면
                int sea_cnt = 0;
                for (int k = 0; k < 4; k++) { // 상하좌우 체크
                    int nx = x + dx[k];
                    int ny = y + dy[k];
                    if (maps[nx][ny] == 0) sea_cnt += 1;
                }
                int upd_iceberg = maps[x][y] - sea_cnt;
                if (upd_iceberg < 0) upd_iceberg = 0;
                upd_maps[x][y] = upd_iceberg;
                if (upd_maps[x][y] > 0) iceberg_cnt += 1; // 업데이트를 했는데도 아직 빙산이 남아있다면, +1
            }
        }
    }
}

void bfs(int x, int y) {
    q.emplace(x, y);
    visited[x][y] = 1;

    while (!q.empty()) {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            if (visited[nx][ny] || upd_maps[nx][ny] <= 0) continue;

            q.emplace(nx, ny);
            visited[nx][ny] = 1;
        }
    }
}

void count_dung() {
    dung_cnt = 0;
    for (int x = 1; x < N - 1; x++) {
        for (int y = 1; y < M - 1; y++) {
            if (visited[x][y]) continue;
            if (upd_maps[x][y] > 0) {
                bfs(x, y);
                dung_cnt += 1;
            }
        }
    }
}

int main() {
    input();

    while (true) {
        melt_iceberg();

        if (iceberg_cnt == 0) { // 빙산이 다 녹아버림
            cout << 0;
            break;
        }

        count_dung();
        answer += 1;

        if (dung_cnt >= 2) {
            cout << answer;
            break;
        }

        memset(visited, 0, sizeof(visited));
        copy_map();
    }

    return 0;
}