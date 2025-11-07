#include<iostream>
#include<queue>
#include<tuple>
using namespace std;

int K, W, H;
int arr[205][205]{};
int visit[205][205][35]{};
int dx[12] = { 0,1,0,-1,-2,-2,-1,-1,1,1,2,2 };
int dy[12] = { 1,0,-1,0,-1,1,-2,2,-2,2,-1,1 };
queue<tuple<int, int, int, int>>q;  // x, y, 이동횟수, 말 점프 카운트

void input() {
	cin >> K >> W >> H;
	for (int i = 0; i < H; i++)
		for (int j = 0; j < W; j++)
			cin >> arr[i][j];
}

void solve() {
	bool flag = false;

	q.push({ 0,0,0,0 });
	
	int ans = 1e9;

	while (!q.empty()) {
		int x = get<0>(q.front());
		int y = get<1>(q.front());
		int time = get<2>(q.front());
		int cnt = get<3>(q.front());
		q.pop();

		if (x == H - 1 && y == W - 1) {
			ans = ans < time ? ans : time;
			flag = true;
		}

		for (int i = 0; i < 4; i++) {  // 인접 이동
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >= 0 && nx < H && ny >= 0 && ny < W) {
				if (!arr[nx][ny] && !visit[nx][ny][cnt]) {
					visit[nx][ny][cnt]++;
					q.push({ nx,ny,time + 1,cnt });
				}
			}
		}
		if (cnt < K)  // 말 점프 사용 가능할 때
			for (int i = 4; i < 12; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx >= 0 && nx < H && ny >= 0 && ny < W) {
					if (!arr[nx][ny] && !visit[nx][ny][cnt + 1]) {
						visit[nx][ny][cnt + 1]++;
						q.push({ nx,ny,time + 1,cnt + 1 });  // 말 점프 카운트 + 1
					}
				}
			}
	}
	if (!flag)
		cout << -1;
	else cout << ans;
}

int main() {
	input();
	solve();

	return 0;
}