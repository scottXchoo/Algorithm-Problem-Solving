#include <bits/stdc++.h>

using namespace std;

int DP[100001] = {1,3};
int mod = 9901;

int main() {
  int N;
  cin >> N;

  for (int i = 2; i <= N; i++) {
    DP[i] = (DP[i-2] + DP[i-1]*2) % mod;
  }

  cout << DP[N];
}