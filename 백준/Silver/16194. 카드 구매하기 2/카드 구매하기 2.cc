#include <iostream>
#include <vector>

using namespace std;

int N;
int card[10001];
int dp[10001];

int main() {
    cin >> N;
    for (int i = 1; i <= N; i++) {
        cin >> card[i];
    }

    dp[1] = card[1];
    for (int i = 2; i <= N; i++) {
        dp[i] = card[i];
        for (int j = 1; j <= i; j++) {
            dp[i] = min(dp[i], dp[i - j] + card[j]);
        }
    }
    cout << dp[N];

    return 0;
}