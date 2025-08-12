#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

#define MAX 21

using namespace std;

int N;
int map[MAX][MAX]{};
int sharkX, sharkY = 0;
int sharkSize = 2;
int eatenFish = 0;
int dx[4] = {0, -1, 0, 1};
int dy[4] = {1, 0, -1, 0};
int visited[MAX][MAX]{};
int shortPath[MAX][MAX]{};
vector<tuple<int, int, int>> fishList;
int answer = 0;

void input() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> map[i][j];
            if (map[i][j] == 9) {
                sharkX = i;
                sharkY = j;
                map[i][j] = 0;
            }
        }
    }
}

void bfs() {
    // 1) 초기화: visited, 최단거리 배열
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            visited[i][j] = 0;
            shortPath[i][j] = 0;
        }
    }

    // 2) BFS로 현재 상어 위치에서 모든 곳의 최단 경로 구하기
    queue<tuple<int, int, int>> q;
    q.push({sharkX, sharkY, 1});

    while (!q.empty()) {
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int dist = get<2>(q.front());
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N || visited[nx][ny]) continue;
            if (map[nx][ny] <= sharkSize) { // 현재는 먹는 것보다는 이동해서 최단경로를 구하는 게 우선!!!
                shortPath[nx][ny] += dist;
                q.push({nx, ny, dist + 1});
                visited[nx][ny]++;
            }
        }
    }

    // 3) 현재 상어가 잡을 수 있는 모든 물고기 구하기
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (map[i][j] > 0 && map[i][j] < sharkSize && map[i][j] != 9 && shortPath[i][j]) {
                fishList.push_back({shortPath[i][j], i, j});
            }
        }
    }
}

void update() {
    // 1) 원래 있던 상어 위치를 0으로 초기화
    map[sharkX][sharkY] = 0;

    // 2) 오름차순 정렬 후, 정보 뽑아내기
    // 최단 거리, 죄표 오름차순 정렬 => 위쪽, 왼쪽 순서
    sort(fishList.begin(), fishList.end());
    int dist = get<0>(fishList.front());
    sharkX = get<1>(fishList.front());
    sharkY = get<2>(fishList.front());

    // 3) 상어 위치 수정 및 업데이트
    map[sharkX][sharkY] = 9;
    answer += dist;
    eatenFish++;
    if (sharkSize == eatenFish) {
        sharkSize++;
        eatenFish = 0;
    }

    fishList.clear();
}

int main() {
    // Input
    input();

    while (true) {
        int isCatch = 0;
        // BFS
        bfs();
        isCatch = fishList.size();
        if (isCatch) {
            // Update
            update();
        } else {
            // Exit
            cout << answer << '\n';
            return 0;
        }
    }
}