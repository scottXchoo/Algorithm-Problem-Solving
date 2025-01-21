#include <iostream>
#include <vector>

using namespace std;
#define MAX 100001

int graph[MAX];
int visited[MAX];
vector<int> tree[MAX];

void dfs(int k) {
    visited[k] = 1;

    for (int i = 0; i < tree[k].size(); i++) {
        int next = tree[k][i];

        if (!visited[next]) {
            graph[next] = k;
            dfs(next);
        }
    }
}

int main() {
    int N;
    cin >> N;

    for (int i = 1; i < N; i++) {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    dfs(1);

    for (int i = 2; i <= N; i++) {
        cout << graph[i] << "\n";
    }

    return 0;
}