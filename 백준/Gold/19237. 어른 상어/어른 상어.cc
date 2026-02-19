#include <iostream>
#include <vector>
#include <array>

#define UP 0
#define DOWN 1
#define LEFT 2
#define RIGHT 3
#define NO_SH (-1)
#define DEBUG 0

using namespace std;
using pos = pair<int, int>; // r, c
using shark = pair<pos, int>; // 위치(r, c), direction

int N, M, K;
pos out_pos = {-1, -1};
vector<vector<pair<int, int>>> s_map;
vector<shark> sharks;
vector<array<array<int, 4>, 4>> s_prior;

void input() {
    cin >> N >> M >> K;

    s_map.assign(N, vector<pair<int, int>>(N, {NO_SH, 0})); // NxN, {idx, remain_time}
    sharks.assign(M, {{0, 0}, 0}); // M, {{r, c}, dir}
    s_prior.assign(M, array<array<int, 4>, 4>()); // M, 벡터 안에 4x4 배열 - 각 상어마다 각 방향마다 우선순위 방향

    for (int r = 0; r < N; r++) { // map 만들기
        for (int c = 0; c < N; c++) {
            int shark_idx = 0;
            cin >> shark_idx; // 0 or 상어 idx
            shark_idx--;
            s_map[r][c].first = shark_idx;
            if (shark_idx != NO_SH) { // 0이 아닌, 상어가 있다면
                s_map[r][c].second = K;
                sharks[shark_idx] = {{r, c}, UP}; // 방향은 UP으로 일단 초기화
            }
        }
    }

    for (auto &shark : sharks) { // 방향 정하기
        cin >> shark.second; // direction
        shark.second--;
    }

    for (auto &p : s_prior) { // 방향 우선순위 정하기
        for (int r = 0; r < 4; r++) {
            for (int c = 0; c < 4; c++) {
                cin >> p[r][c];
                p[r][c]--;
            }
        }
    }
}

pos next_pos(const pos &c_pos, int c_dir) {
    pos next = c_pos;
    switch (c_dir) {
        case UP:
            next.first -= 1;
            break;
        case DOWN:
            next.first += 1;
            break;
        case LEFT:
            next.second -= 1;
            break;
        case RIGHT:
            next.second += 1;
            break;
        default: ;
    }
    if (next.first >= 0 && next.first < N && next.second >= 0 && next.second < N) return next;
    return {-1, -1};
}

int main() {
    input();

    int answer = 1;
    auto reserved = vector<shark>(M, {{0, 0}, 0}); // M, {{r, c}, dir}
    while (answer <= 1000) {
        // 상어 움직임
        for (int idx = 0; idx < M; idx++) {
            auto [c_pos, c_dir] = sharks[idx];
            if (c_pos == out_pos) continue; // Out된 상어라면, 넘어가기

            int is_moved = 0;
            int first_matched_dir = -1;
            for (auto &next_dir : s_prior[idx][c_dir]) {
                auto n_pos = next_pos(c_pos, next_dir);
                if (n_pos == out_pos) continue;

                const int n_r = n_pos.first;
                const int n_c = n_pos.second;
                if (s_map[n_r][n_c].first == NO_SH) { // 다음 위치에 냄새 없음
                    reserved[idx] = {n_pos, next_dir}; // reserved에 저장
                    is_moved = 1;
                    break;
                }
                if (s_map[n_r][n_c].first == idx && first_matched_dir == -1) { // 다음 위치가 자신인데, 아직 방향이 정해지지 X
                    first_matched_dir = next_dir;
                }
            }
            if (!is_moved && first_matched_dir != -1) {
                reserved[idx] = {next_pos(c_pos, first_matched_dir), first_matched_dir};
            }
        }

        // 맵 전체 k 감소
        for (auto &row : s_map) {
            for (auto &element : row) {
                if (element.first != NO_SH) {
                    element.second--; // 냄새 감소
                    if (element.second == 0) element.first = NO_SH; // 냄새가 0이면, 해당 위치의 idx도 NO로 변경
                }
            }
        }

        // 맵 업데이트 (상어 겹치는지)
        for (int idx = 0; idx < M; idx++) {
            if (sharks[idx].first == out_pos) continue;

            auto [c_pos, c_dir] = reserved[idx];
            const int c_r = c_pos.first;
            const int c_c = c_pos.second;
            const auto c_shark = s_map[c_r][c_c].first; // 해당 위치에 있는 상어 여부
            if (c_shark == NO_SH || s_map[c_r][c_c].second < K) { // 상어 없거나 남은 시간이 K보다 작으면(없다는 뜻)
                s_map[c_r][c_c] = {idx, K}; // map 업데이트
                sharks[idx].first = c_pos;
                sharks[idx].second = c_dir;
            } else if (c_shark > idx) { // 잡아먹을 수 있음
                s_map[c_r][c_c] = {idx, K}; // map 업데이트
                sharks[idx].first = out_pos;
            } else { // 잡아먹힘
                sharks[idx].first = out_pos; // map 업데이트 X
            }
        }

        // End: 상어 1만 남았는지
        int remain_cnt = 0;
        for (auto &shark : sharks) {
            if (shark.first != out_pos) {
                remain_cnt++;
            }
        }

        if (remain_cnt == 1) break;
        answer++;
    }

    cout << ((answer > 1000) ? -1 : answer) << '\n';
    return 0;
}
