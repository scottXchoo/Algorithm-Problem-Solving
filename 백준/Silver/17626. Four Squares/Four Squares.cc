#include <bits/stdc++.h>

using namespace std;

int dp[500002];
int N;

int main() {
  cin.tie(0)->sync_with_stdio(0);
  
  int n, imsi_N, cnt, min_cnt;

  cin >> N;

  dp[0] = 0;  //1,4,9,16,25, ... 제곱수를 위함
  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 3;
  dp[4] = 1;

  for (int i = 5; i <= N; i++) {
	n = floor(sqrt(i));
	min_cnt = 4;

	for (int j = 1; j <= n; j++) {
	  imsi_N = i - j * j;
	  cnt = dp[imsi_N] + 1;
	  if (cnt < min_cnt) {
		min_cnt = cnt;
	  }
	}
	dp[i] = min_cnt;
  }

  cout << dp[N];

}