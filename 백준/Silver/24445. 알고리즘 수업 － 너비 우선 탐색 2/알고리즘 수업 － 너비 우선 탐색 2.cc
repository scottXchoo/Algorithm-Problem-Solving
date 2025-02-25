#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#define MAX 200001
using namespace std;

int visited[MAX];
vector<int> graph[MAX];
int answer[MAX];

int main() {
    int N, M, R;
    cin >> N >> M >> R;
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    queue<int> q;
    visited[R] = 1;
    q.push(R);
    int index = 1;
    answer[R] = index;
    while (!q.empty()) {
        int n_n = q.front();
        q.pop();

        // graph[n_n] 정렬 필요
        sort(graph[n_n].begin(), graph[n_n].end(), greater<int>());
        for (int nn_n : graph[n_n]) {
            if (visited[nn_n]) continue;
            visited[nn_n] = 1;
            q.push(nn_n);
            index++;
            answer[nn_n] = index;
        }
    }

    for (int i = 1; i <= N; i++) {
        cout << answer[i] << '\n';
    }

    return 0;
}