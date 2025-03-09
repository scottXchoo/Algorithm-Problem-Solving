#include <iostream>
#include <algorithm>

using namespace std;

int tri[501][501] = {0};
int dp[501][501] = {0};

int main() {
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= i; j++) {
            cin >> tri[i][j];
        }
    }

    dp[1][1] = tri[1][1];
    for (int i = 2; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j];
        }
    }

    int result = -1;
    for (int i = 1; i <= N; i++) {
        if (result < dp[N][i]) {
            result = dp[N][i];
        }
    }
    cout << result;

    return 0;
}
