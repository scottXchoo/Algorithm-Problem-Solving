#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define first f;
#define second s;
ll n, m, a[300004], ret = 1e18;

bool check(ll mid) {
    ll num = 0;
    for(int i = 0; i < m; i++) {
        num += a[i] / mid;
        if(a[i] % mid) num++;
    }
    return n >= num;
}

int main() {
    cin >> n >> m;
    ll lo = 1, hi = 0, mid;
    for(int i = 0; i < m; i++) cin >> a[i], hi = max(hi, a[i]);
    
    while(lo <= hi) {
        mid = (lo + hi) / 2;
        if(check(mid)) {
            ret = min(ret, mid);
            hi = mid - 1;
        } else lo = mid + 1;
    }
    cout << ret << "\n";
    return 0;
}