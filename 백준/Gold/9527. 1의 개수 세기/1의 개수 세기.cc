#include <iostream>
#define MAX 55

using ll = long long;
using namespace std;

ll power[MAX];
ll A, B;
ll ans = 0;

ll calculate(ll x) {
  ll ret = x & 1;
  for (int i = MAX - 1; i > 0; i--) {
	if (x & (1LL << i)) {
	  ret += power[i - 1] + (x - (1LL << i) + 1);
	  x -= 1LL << i;
	}
  }
  return ret;
}

int main() {
  power[0] = 1;
  for (ll i = 1; i < MAX; i++) {
	power[i] = power[i - 1] * 2 + (1LL << i);
  }

  cin >> A >> B;

  ans = calculate(B) - calculate(A - 1);
  cout << ans << '\n';

  return 0;
}