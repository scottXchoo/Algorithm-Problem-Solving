#include <bits/stdc++.h>
using namespace std;

vector<int> adj[10001];
int dp[10001], visited[10001], n, m, a, b, mx;

// DFS 로직 암기하기
int dfs(int here) {
    // 탐색 시작하는 정점을 바로 방문처리 하기
    visited[here] = 1;
    int ret = 1;
    // 그래프 adj와 연결된 정점들 탐색하기
    for(int there : adj[here]) {
        if(visited[there]) continue;
        // 연결된 정점들 몇 개인지 누적 합 구하기
        ret += dfs(there);
    }
    return ret;
}

int main() {
    // #0. 입력 부분
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    // 0-1. 그래프 만들기
    while(m--) {
        cin >> a >> b;
        adj[b].push_back(a);
    }
    // #1. 모든 정점 탐색하기
    for(int i = 1; i <= n; i++) {
        // 1-1. 탐색할 때마다, 초기화 필요
        fill(visited, visited + 10001, 0);
        // 1-2. 배열에 dfs 값 넣기
        dp[i] = dfs(i);
        mx = max(dp[i], mx);
    }
    // #2. max 값과 같은 요소들만 출력하기
    for(int i = 1; i <= n; i++) if(mx == dp[i]) cout << i << " ";
    return 0;
}