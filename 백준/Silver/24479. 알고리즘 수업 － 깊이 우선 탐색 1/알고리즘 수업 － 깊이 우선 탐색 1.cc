#include <iostream>
#include <algorithm>

#define MAX 200001
using namespace std;

vector<int> graph[MAX];
int visited[MAX];
int answer[MAX];
int seq = 1;

void dfs(int n_n, int depth) {
    sort(graph[n_n].begin(), graph[n_n].end());
    for (int nn_n : graph[n_n]) {
        if (visited[nn_n]) continue;
        answer[nn_n] = ++seq;
        visited[nn_n] = 1;
        dfs(nn_n, depth+1);
    }
}

int main() {
    int N, M, R;
    cin >> N >> M >> R;
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    visited[R] = 1;
    answer[R] = seq;
    dfs(R, 0);
    for (int i = 1; i <= N; i++) {
        cout << answer[i] << '\n';
    }

    return 0;
}