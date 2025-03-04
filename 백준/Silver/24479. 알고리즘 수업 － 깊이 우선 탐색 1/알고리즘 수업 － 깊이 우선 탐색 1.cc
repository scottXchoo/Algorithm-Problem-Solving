#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

int main()
{
    int N, M, R;
    cin >> N >> M >> R; // 정점수, 간선 수, 시작 정점

    vector<vector<int> > edges(N);
    vector<bool> visited(N, false);
    vector<int> orders(N, 0);

    int source, destination;
    for (int i = 0; i < M; i++)
    {
        cin >> source >> destination;
        edges[source-1].push_back(destination);
        edges[destination-1].push_back(source);
    }

    for (int i = 0; i < N; i++)
    {
        sort(edges[i].begin(), edges[i].end(), std::greater<int>());
    }

    stack<int> node_s;
    node_s.push(R);

    int order = 1;
    while (!node_s.empty())
    {
        int current_node = node_s.top(); node_s.pop();
        if (visited[current_node-1]) continue;
        visited[current_node-1] = true;
        orders[current_node-1] = order++;
        for (auto adj_node: edges[current_node-1])
        {
            if (!visited[adj_node-1])
            {
                node_s.push(adj_node);
            }
        }
    }

    for (auto result: orders)
    {
        cout << result << '\n';
    }

    return 0;
}