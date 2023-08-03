#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, b;
	cin >> n >> b;

	string b_num;
	while(n != 0) {
		int tmp = n % b;
		if (tmp > 9) {
			tmp = tmp - 10 + 'A';
			b_num += tmp;
		} else {
			b_num += ('0' + tmp);
		}
		n /= b;
	}
	reverse(b_num.begin(), b_num.end());
	cout << b_num << '\n';
	return 0;
}