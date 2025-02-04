#include <iostream>
#include <algorithm> // std::min을 사용하기 위해 필요
using namespace std;

int main() {
    int a[1001], dp[1001];
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        dp[i] = 100001;
    }

    dp[0] = 0;
    for (int i = 0; i < n; i++) {
        if (dp[i] == 100001) continue; // 아직 도달할 수 없는 위치라면 건너뛰기
        for (int j = 1; j <= a[i]; j++) {
            if (i + j < n) { // 배열 범위 체크
                dp[i + j] = min(dp[i + j], dp[i] + 1);
            }
        }
    }

    if (dp[n - 1] == 100001)
        cout << "-1";
    else
        cout << dp[n - 1];

    return 0;
}
