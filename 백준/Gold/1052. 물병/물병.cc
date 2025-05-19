#include <iostream>

using namespace std;

int main() {
    int N, K;
    cin >> N >> K;

    int ans = 0;
    while (true) {
        int temp = N;
        int firstIdx = -1;

        int cnt = 0;
        int idx = 0;
        while (temp) {
            if (temp & 1) {
                if (firstIdx == -1) firstIdx = idx;
                cnt++;
            }
            idx++;
            temp >>= 1;
        }

        if (cnt <= K) break;
        N += (1 << firstIdx);
        ans += (1 << firstIdx);
        
    }

    cout << ans;

    return 0;
}