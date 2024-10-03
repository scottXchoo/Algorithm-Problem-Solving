#include <iostream>
#include <vector>
#define MAX 1001
using namespace std;

int N, M;
vector<int> graph[MAX];
int visited[MAX];

void DFS(int node) {
  visited[node] = 1;

  for (int n_node : graph[node]) {
	if (visited[n_node]) continue;
	DFS(n_node);
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  cin >> N >> M;

  // Graph 만들기
  int u, v;
  for (int i = 0; i < M; i++) {
	cin >> u >> v;
	graph[u].push_back(v);
	graph[v].push_back(u);
  }

  // DFS 탐색
  int ans = 0;
  for (int i = 1; i <= N; i++) {
	if (visited[i] == 0) {
	  ans++;
	  DFS(i);
	}
  }

  cout << ans << '\n';

  return 0;
}