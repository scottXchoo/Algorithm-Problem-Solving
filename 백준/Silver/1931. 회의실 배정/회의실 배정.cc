#include <bits/stdc++.h>
using namespace std;

int from, to, n, idx = 0, ret = 1;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    vector<pair<int, int>> v;
    for(int i = 0; i < n; i++) {
        cin >> from >> to;
        v.push_back({to, from});
    }
    // 끝 시간을 순서대로 정렬하기
    sort(v.begin(), v.end());
    from = v[0].second;
    to = v[0].first;
    // 그 다음 교차하는 지점들 처리하기
    for(int i = 1; i < n; i++) {
        if(v[i].second < to) continue;
        from = v[i].second; to = v[i].first; ret++;
    }
    cout << ret << '\n';
    return 0;
}