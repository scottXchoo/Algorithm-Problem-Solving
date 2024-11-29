#include <iostream>
#include <vector>
#include <queue>
#define MAX 1001
#define INF 987654321

using namespace std;

int N, M;
int dist[MAX];
vector<pair<int, int>> graph[MAX];
int s_node, e_node;

int main() {
  cin >> N >> M;

  for (int i = 0; i < M; i++) {
	int v1, v2, cost;
	cin >> v1 >> v2 >> cost;
	graph[v1].emplace_back(cost, v2); // 버스가 한 쪽 방향으로만 가기에 양방향(무방향) X & 단방향 O
  }

  cin >> s_node >> e_node;

  fill(dist, dist + MAX, INF); // dist 배열 초기화 반드시!!!
  priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq; // 오름차순 가능

  pq.emplace(0, s_node);
  dist[s_node] = 0;

  while (!pq.empty()) {
	int cur_cost = pq.top().first;
	int cur_node = pq.top().second;
	pq.pop();

	if (dist[cur_node] < cur_cost) continue;

	for (auto &i : graph[cur_node]) {
	  int next_cost = cur_cost + i.first;
	  int next_node = i.second;

	  if (dist[next_node] > next_cost) {
		dist[next_node] = next_cost;
		pq.emplace(next_cost, next_node);
	  }
	}
  }

  cout << dist[e_node];

  return 0;
}