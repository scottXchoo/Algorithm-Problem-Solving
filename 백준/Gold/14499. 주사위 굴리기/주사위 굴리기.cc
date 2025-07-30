#include <iostream>

using namespace std;

int N, M, x, y, K;
int map[21][21]{};
int dice[4][3]{};
int dx[5] = {0, 0, 0, -1, 1};
int dy[5] = {0, 1, -1, 0, 0};

void input() {
    cin >> N >> M >> x >> y >> K;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> map[i][j];
        }
    }
}

int is_out(int nx, int ny) {
    if (nx < 0 || ny < 0 || nx >= N || ny >= M) {
        return 1;
    }
    return 0;
}

void updateDice(int order) {
    if (order == 1) {
        int tmp = dice[3][1];
        dice[3][1] = dice[1][2];
        dice[1][2] = dice[1][1];
        dice[1][1] = dice[1][0];
        dice[1][0] = tmp;
    } else if (order == 2) {
        int tmp = dice[3][1];
        dice[3][1] = dice[1][0];
        dice[1][0] = dice[1][1];
        dice[1][1] = dice[1][2];
        dice[1][2] = tmp;
    } else if (order == 3) {
        int tmp = dice[3][1];
        dice[3][1] = dice[0][1];
        dice[0][1] = dice[1][1];
        dice[1][1] = dice[2][1];
        dice[2][1] = tmp;
    } else {
        int tmp = dice[3][1];
        dice[3][1] = dice[2][1];
        dice[2][1] = dice[1][1];
        dice[1][1] = dice[0][1];
        dice[0][1] = tmp;
    }
}

void func() {
    if (map[x][y] == 0) {
        map[x][y] = dice[3][1];
    } else {
        dice[3][1] = map[x][y];
        map[x][y] = 0;
    }
    cout << dice[1][1] << '\n';
}

int main() {
    input();

    for (int i = 0; i < K; i++) {
        int order;
        cin >> order;

        int nx = x + dx[order];
        int ny = y + dy[order];
        if (is_out(nx, ny)) continue;

        // 주사위 숫자 업데이트
        updateDice(order);

        // 좌표 업데이트
        x += dx[order];
        y += dy[order];

        // 이동한 상황 처리
        func();

    }
    return 0;
}