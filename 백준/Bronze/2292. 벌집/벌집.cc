#include <iostream>

using namespace std;

int main() {
  int lineNum = 1;
  int baseNum = 1;
  int N;
  int answer = 0;

  cin >> N;

  if (N == 1) answer = 1;

  while (true) {
	if (baseNum >= N) {
	  answer = lineNum;
	  break;
	}

	baseNum += 6 * lineNum;
	lineNum++;
  }

  cout << answer;

  return 0;
}