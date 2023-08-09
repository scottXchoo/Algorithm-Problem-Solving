#include <bits/stdc++.h>
using namespace std;

int main(void) {
	int N = 0;
	int cnt = 0;
	cin >> N;
	
	for(int i = 5; i <= N; i *= 5) {
		cnt += (N / i);
	}
	cout << cnt;

	return 0;
}