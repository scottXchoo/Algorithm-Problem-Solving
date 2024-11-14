#include <iostream>

using namespace std;

int main() {
  std::ostream::sync_with_stdio(false);

  int N;
  cin >> N;

  int dp[1001] = {0, 1, 2};
  for (int i = 3; i <= N; i++) {
	dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
  }
  
  cout << dp[N];

  return 0;
}