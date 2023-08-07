#include <bits/stdc++.h>
using namespace std;

int N, ans, cnt, tmp;

int main() {
  cin >> N;
  ans = 0;
  cnt = 0;
  while(cnt != N) {
      ans++;
      tmp = ans;
      while(tmp != 0) {
          if(tmp % 1000 == 666) {
              cnt++;
              break;
          } else tmp /= 10;
      }
  }
  cout << ans;
}