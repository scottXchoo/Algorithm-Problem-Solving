#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <cstring>

using namespace std;

#define MAX 1001

int N, M;
int H_x, H_y;
int E_x, E_y;
int maps[MAX][MAX] {};
int new_maps[MAX][MAX] {};
vector<pair<int, int>> walls;
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
int visited[MAX][MAX][2] {};
int answer = 1000001;

void input() {
    cin >> N >> M;
    cin >> H_x >> H_y;
    cin >> E_x >> E_y;
    for (int i = 1; i <= N; i ++) {
        for (int j = 1; j <= M; j++) {
            cin >> maps[i][j];
            if (maps[i][j] == 1) {
                walls.emplace_back(i, j);
            }
        }
    }
}

void old_to_new_maps() {
    for (int i = 1; i <= N; i ++) {
        for (int j = 1; j <= M; j++) {
            new_maps[i][j] = maps[i][j];
        }
    }
}

void bfs() {
    queue<pair<pair<int, int>, pair<int, int>>> q;
    q.push({{H_x, H_y}, {0, 1}});

    while (!q.empty()) {
        int cx = q.front().first.first;
        int cy = q.front().first.second;
        int dist = q.front().second.first;
        int key = q.front().second.second;
        q.pop();

        if (E_x == cx && E_y == cy) {
            cout << dist;
            return;
        }
        if (visited[cx][cy][key]) continue;
        visited[cx][cy][key] = 1;

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            if (nx <= 0 || ny <= 0 || nx > N || ny > M) continue;
            if (maps[nx][ny] == 1 && key == 1) q.push({{nx, ny}, {dist + 1, 0}});
            if (maps[nx][ny] == 0) q.push({{nx, ny}, {dist + 1, key}});
        }
    }

    cout << "-1";
}

int main() {
    input();
    bfs();
    return 0;
}