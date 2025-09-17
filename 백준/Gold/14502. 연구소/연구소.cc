#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

#define MAX 10

int N, M;
int maps[MAX][MAX];
int temp[MAX][MAX];
int visited[MAX][MAX];
int dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
int answer = 0;

void copy(int temp[MAX][MAX], int maps[MAX][MAX]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            temp[i][j] = maps[i][j];
        }
    }
}

void bfs() {
    int after[MAX][MAX];
    copy(after, temp);

    // Virus 위치 넣기
    queue<pair<int, int>> q;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (after[i][j] == 2) q.push({i, j});
        }
    }

    // Virus 퍼뜨리기
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            if (after[nx][ny] == 0) {
                after[nx][ny] = 2;
                q.push({nx, ny});
            }
        }
    }

    //  안전구역 업데이트
    int cnt = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (after[i][j] == 0) cnt++;
        }
    }
    answer = max(answer, cnt);
}


void wall(const int cur) {
    if (cur == 3) {
        // 새 벽이 3개 세워지면, bfs 돌기
        bfs();
        return;
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (temp[i][j] == 0) {
                temp[i][j] = 1;
                wall(cur + 1);
                temp[i][j] = 0;
            }
        }
    }
}

int main() {
    // 입력
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> maps[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (maps[i][j] == 0) {
                memset(visited, 0, sizeof(visited));
                // 실제 map을 temp로 복사
                copy(temp, maps);
                // 새 벽을 하나 세우기
                temp[i][j] = 1;
                // 나머지 두 개의 새 벽 세우기
                wall(1);
                // 원상복귀
                temp[i][j] = 0;
            }
        }
    }

    cout << answer;
}