#include <bits/stdc++.h>
using namespace std;

vector<int> adj[10001];
int dp[10001], visited[10001], n, m, a, b, mx;

int dfs(int here) {
    visited[here] = 1;
    int ret = 1;
    for(int there : adj[here]) {
        if(visited[there]) continue;
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
        memset(visited, 0, sizeof(visited));
        dp[i] = dfs(i);
        mx = max(dp[i], mx);
    }
    for(int i = 1; i <= n; i++) if(mx == dp[i]) cout << i << " ";
    return 0;
}