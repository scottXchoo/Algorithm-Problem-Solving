#include<bits/stdc++.h>
using namespace std;

int n, m, j, l, r, tmp, ret;
int main() {
    cin >> n >> m >> j;
    l = 1;
    for(int i = 0; i < j; i++) {
        r = l + m - 1;
        cin >> tmp;
        if(tmp >= l && tmp <= r) continue;
        else {
            if(tmp < l) {
                ret += (l - tmp);
                l = tmp;
            } else {
                l += (tmp - r);
                ret += (tmp - r);
            }
        }
    }
    cout << ret << '\n';
    return 0;
}