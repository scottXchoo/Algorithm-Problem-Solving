#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

#define ROW 12
#define COL 6

char maps[ROW][COL];
bool visited[ROW][COL];

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};

bool flag = false;
int answer = 0;
int temp_cnt = 0;

queue<pair<int, int>> q;
vector<pair<int, int>> puyo_temp, puyo_vec;

void input() {
    for (int i = 0; i < ROW; i++) {
        for (int j = 0; j < COL; j++) {
            cin >> maps[i][j];
        }
    }
}

void bfs() {
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        visited[x][y] = true;
        puyo_temp.push_back(make_pair(x, y));

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= ROW || ny >= COL) continue;
            if (maps[nx][ny] == '.') continue;
            if (visited[nx][ny] == true) continue;
            if (maps[nx][ny] != maps[x][y]) continue;

            temp_cnt += 1;
            visited[nx][ny] = true;
            q.push(make_pair(nx, ny));
        }
    }
}

void update() {
    for (int i = 0; i < puyo_vec.size(); i++) {
        int x = puyo_vec[i].first;
        int y = puyo_vec[i].second;

        maps[x][y] = '.';
    }
}

void down() {
    for (int i = ROW - 1; i >= 0; i--) {
        for (int j = COL - 1; j >= 0; j--) {
            if (maps[i][j] == '.') continue;
            int temp = i;

            while (1) {
                // temp가 끝까지 내려왔거나, 다음 칸에 Puyo가 있거나
                if (temp == ROW - 1 || maps[temp + 1][j] != '.') break;

                maps[temp + 1][j] = maps[temp][j];
                maps[temp][j] = '.';
                temp++;
            }
        }
    }
}

int main() {
    input();

    while (1) {
        flag = false;
        memset(visited, false, sizeof(visited));
        puyo_vec.clear();

        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                // '.' 이거나 방문한 곳은 스킵
                if (maps[i][j] == '.' || visited[i][j]) continue;

                temp_cnt = 1;
                q.push(make_pair(i, j));
                bfs();

                if (temp_cnt >= 4) {
                    flag = true; // 펑!

                    // 좌표 옮기기: puyo_temp => puyo_vec
                    for (int k = 0; k < puyo_temp.size(); k++) {
                        puyo_vec.push_back(puyo_temp[k]);
                    }
                }
                puyo_temp.clear();
            }
        }
        update(); // 터진 뿌요 없애기
        down(); // 공간 아래로 내리기

        if (flag == true) answer++;
        else break;
    }

    cout << answer;

    return 0;
}