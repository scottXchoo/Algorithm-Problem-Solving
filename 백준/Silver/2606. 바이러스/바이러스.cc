#include <iostream>
#include <queue>
#define MAX 101

using namespace std;

// BFS에 필요한 재료들
int graph[MAX][MAX];
int visited[MAX] = {0,};
queue<int> q;

// 입력 변수들
int N, M;
int ans = 0;

void bfs(int s) {
  // 1. Queue에 시작 노드 넣고 방문 처리
  q.push(s); // 큐 제일 뒤에 원소 추가
  visited[s] = 1;

  // 2. Queue가 빌 때까지 while문 돌기
  while (!q.empty()) {
	int c = q.front(); // 큐 제일 앞에 있는 원소 반환
	q.pop(); // 큐 제일 앞에 있는 원소 삭제

	// c 노드를 기준으로 다른 노드들 다 한 번씩 체크!
	for (int i = 1; i <= N; i++) {
	  if (visited[i] == 1 || graph[c][i] != 1) continue;

	  q.push(i);
	  visited[i] = 1;
	  ans++;
	}
  }
}

int main() {
  cin >> N >> M;

  for (int i = 0; i < M; i++) {
	int start, end;
	cin >> start >> end;

	// 어떤 식으로 그래프를 만들지?
	graph[start][end] = 1;
	graph[end][start] = 1;
  }

  bfs(1);

  cout << ans;

  return 0;
}