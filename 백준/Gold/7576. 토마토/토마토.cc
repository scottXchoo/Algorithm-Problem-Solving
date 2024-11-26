#include <iostream>
#include <queue>

using namespace std;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int tomato[1002][1002];
int dist[1002][1002];

int days = 0;

int main() {
  int M, N;
  cin >> M >> N;

  queue<pair<int, int>> q;
  for (int i = 0; i < N; i++) {
	for (int j = 0; j < M; j++) {
	  cin >> tomato[i][j];
	  dist[i][j] = -1;
	  if (tomato[i][j] == 1) {
		q.emplace(i, j);
		dist[i][j] = 0;
	  }
	}
  }

  while (!q.empty()) {
	pair<int, int> cur = q.front();
	q.pop();

	for (int i = 0; i < 4; i++) {
	  int nx = cur.first + dx[i];
	  int ny = cur.second + dy[i];

	  if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

	  if (tomato[nx][ny] == 0 && dist[nx][ny] == -1) {
		q.emplace(nx, ny);
		dist[nx][ny] = dist[cur.first][cur.second] + 1;
	  }
	}
  }

  for (int i = 0; i < N; i++) {
	for (int j = 0; j < M; j++) {
	  if (tomato[i][j] == 0 && dist[i][j] == -1) {
		cout << -1;
		return 0;
	  }
	  days = max(days, dist[i][j]);
	}
  }

  cout << days;

  return 0;
}