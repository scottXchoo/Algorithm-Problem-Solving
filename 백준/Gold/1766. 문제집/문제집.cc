#include<iostream>
#include<vector>
#include<queue>

using namespace std;

int main() {
  int N, M;
  cin >> N >> M;

  // 1. indegree를 기록하며 vector 그래프를 만든다.
  vector<int> inDegree(N + 1);
  vector<vector<int>> graph(N + 1);
  for (int i = 0; i < M; i++) {
	int a, b;
	cin >> a >> b;

	inDegree[b]++;
	graph[a].push_back(b);
  }

  // 2. indegree가 0인 정점을 prority_queue에 넣는다.
  priority_queue<int, vector<int>, greater<>> pq;
  for (int i = 1; i <= N; i++) {
	if (inDegree[i] == 0) {
	  pq.push(i);
	}
  }

  // 3. queue에서 꺼내서 출력 후, 해당 cur 연결된 문제의 indegree를 1 줄인다.
  while (!pq.empty()) {
	int cur = pq.top();
	pq.pop();
	cout << cur << ' ';

	for (int next : graph[cur]) {
	  inDegree[next]--;
	  // 4. indegree가 0이 되면 priority_queue에 넣는다.
	  if (inDegree[next] == 0) {
		pq.push(next);
	  }
	}
  }

  return 0;
}