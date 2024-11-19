#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  std::ostream::sync_with_stdio(false);

  int N;
  cin >> N;

  vector<int> aV, bV, cV, dV;
  for (int i = 0; i < N; i++) {
	int a, b, c, d;
	cin >> a >> b >> c >> d;
	aV.push_back(a);
	bV.push_back(b);
	cV.push_back(c);
	dV.push_back(d);
  }

  vector<int> abV, cdV;
  for (int i = 0; i < N; i++) {
	for (int j = 0; j < N; j++) {
	  abV.push_back(aV[i] + bV[j]);
	  cdV.push_back(cV[i] + dV[j]);
	}
  }

  sort(abV.begin(), abV.end());
  sort(cdV.begin(), cdV.end(), greater<>());

  long long answer = 0;
  long long size = N * N;
  int left = 0, right = 0;
  while (left < size && right < size) {
	if (abV[left] + cdV[right] == 0) {
	  long long leftCnt = 1, rightCnt = 1;
	  left++, right++;

	  while (left < size && abV[left - 1] == abV[left]) {
		left++;
		leftCnt++;
	  }

	  while (right < size && cdV[right - 1] == cdV[right]) {
		right++;
		rightCnt++;
	  }

	  answer += leftCnt * rightCnt;
	} else if (abV[left] + cdV[right] < 0) {
	  left++;
	} else {
	  right++;
	}
  }

  cout << answer;

  return 0;
}