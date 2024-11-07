#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
using namespace std;

int main() {
  cin.tie(0)->sync_with_stdio(0);

  int N, M;
  cin >> N >> M;

  int board[501][501];
  queue<pair<pair<int, int>, pair<int, int>>> blocks;
  for (int i = 0; i < N; i++) {
	for (int j = 0; j < M; j++) {
	  cin >> board[i][j];
	  blocks.push({{i, j}, {i + 1, j}});
	  blocks.push({{i, j}, {i, j + 1}});
	}
  }

  int answer = 0;
  int dx[] = {0, 0, -1, 1};
  int dy[] = {-1, 1, 0, 0};
  while (!blocks.empty()) {
	int x1, y1, x2, y2;
	tie(x1, y1) = blocks.front().first;
	tie(x2, y2) = blocks.front().second;
	blocks.pop();

	vector<pair<int, int>> v;
	for (int i = 0; i < 4; i++) {
	  int nx1 = x1 + dx[i];
	  int ny1 = y1 + dy[i];

	  if (nx1 < 0 || nx1 >= N || ny1 < 0 || ny1 >= M) continue;
	  if (nx1 == x2 && ny1 == y2) continue;

	  v.emplace_back(nx1, ny1);
	}
	for (int i = 0; i < 4; i++) {
	  int nx2 = x2 + dx[i];
	  int ny2 = y2 + dy[i];

	  if (nx2 < 0 || nx2 >= N || ny2 < 0 || ny2 >= M) continue;
	  if (nx2 == x1 && ny2 == y1) continue;

	  v.emplace_back(nx2, ny2);
	}

	int sum = 0;
	for (int i = 0; i < v.size() - 1; i++) {
	  for (int j = i + 1; j < v.size(); j++) {
		int nx1 = v[i].first;
		int ny1 = v[i].second;
		int nx2 = v[j].first;
		int ny2 = v[j].second;

		sum = max(sum, board[nx1][ny1] + board[nx2][ny2]);
	  }
	}
	answer = max(answer, sum + board[x1][y1] + board[x2][y2]);
  }

  cout << answer << '\n';

  return 0;
}