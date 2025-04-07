#include <iostream>
#include <queue>
using namespace std;
typedef long long ll;

int main() {
    priority_queue<ll, vector<ll>, greater<ll> > pq;

    int N, M;
    cin >> N >> M;

    for (int i = 0; i < N; i++) {
        ll input;
        cin >> input;
        pq.push(input);
    }

    while (M--) {
        ll first = pq.top();
        pq.pop();
        ll second = pq.top();
        pq.pop();
        ll sum = first + second;
        pq.push(sum);
        pq.push(sum);
    }

    ll ans = 0;
    while (!pq.empty()) {
        ans += pq.top();
        pq.pop();
    }
    
    cout << ans << '\n';

    return 0;
}