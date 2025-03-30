#include <iostream>

using namespace std;

int dp[100001][3];
int mod = 9901;

int main() {
    int N;
    cin >> N;
    dp[0][0] = 1;
    dp[0][1] = 1;
    dp[0][2] = 1;

    for (int i = 1; i < N; i++) {
        dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % mod;
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod;
        dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % mod;
    }

    const int answer = (dp[N-1][0] + dp[N-1][1] + dp[N-1][2]) % mod;
    cout << answer << '\n';

    return 0;
}