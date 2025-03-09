#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<pair<int, int> > v;
priority_queue<int, vector<int>, greater<int> > pq;

int main() {
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int start, end;
        cin >> start >> end;
        v.emplace_back(start, end);
    }
    sort(v.begin(), v.end());
    pq.push(v[0].second); // 시작 시간이 가장 낮은 회의의 끝 시간 넣기

    int ans = 1;
    for (int i = 1; i < N; i++) {
        while (!pq.empty() && pq.top() <= v[i].first) {
            pq.pop(); // 기존 회의 끝나서 pq에서 빼주기
        }
        pq.push(v[i].second); // pq에 다음 회의 넣어주기
        ans = max(ans, static_cast<int>(pq.size()));
    }

    cout << ans;

    return 0;
}