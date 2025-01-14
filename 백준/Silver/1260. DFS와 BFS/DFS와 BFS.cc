#include <iostream>
#include <queue>
#include <string.h>

using namespace std;
#define MAX 1001

int graph[MAX][MAX];
int visited[MAX];

int N, M, V;

void dfs(int V) {
    visited[V] = 1;
    cout << V << " ";

    for (int i = 1; i <= N; i++) {
        if (graph[V][i] == 1 && visited[i] == 0) {
            dfs(i);
        }
        if (i == N) return;
    }
}

void bfs(int V) {
    queue<int> q;
    q.push(V);

    while (!q.empty()) {
        int next = q.front();
        q.pop();

        visited[next] = 1;
        cout << next << " ";

        for (int i = 1; i <= N; i++) {
            if (graph[next][i] == 1 && visited[i] == 0) {
                q.push(i);
                visited[i] = 1;
            }
        }
    }
}

int main() {
    cin >> N >> M >> V;

    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        graph[u][v] = 1;
        graph[v][u] = 1;
    }

    dfs(V);

    cout << '\n';
    memset(visited, 0, sizeof(visited));

    bfs(V);

    return 0;
}