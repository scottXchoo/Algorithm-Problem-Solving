#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>

#define MAX 200001
#define LL long long int
using namespace std;

LL visited[MAX];
LL answer[MAX];
vector<int> graph[MAX];

int main() {
    int N, M, R;
    cin >> N >> M >> R;
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int index = 1;
    memset(visited, -1, sizeof(visited));

    queue<int> q;
    q.push(R);
    visited[R] = 0;
    answer[R] = index;
    while (!q.empty()) {
        int n_n = q.front();
        q.pop();

        sort(graph[n_n].begin(), graph[n_n].end());
        for (int nn_n : graph[n_n]) {
            if (visited[nn_n] != -1) continue;
            q.push(nn_n);
            visited[nn_n] = visited[n_n] + 1;
            answer[nn_n] = ++index;
        }
    }

    LL ans = 0;
    for (int i = 1; i <= N; i++) {
        ans += answer[i] * visited[i];
    }
    cout << ans;

    return 0;
}