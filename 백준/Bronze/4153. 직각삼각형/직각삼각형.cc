#include <iostream>

using namespace std;

int main() {
  int a, b, c;

  while(true) {
	int temp = 0;
	cin >> a >> b >> c;

	if (a == 0 || b == 0 || c == 0) break;

	// 스왑 - 오름차순 정렬
	if (a > b) {
	  temp = b;
	  b = a;
	  a = temp;
	}
	if (b > c) {
	  temp = c;
	  c = b;
	  b = temp;
	}

	if (c*c == a*a + b*b) {
	  cout << "right \n";
	} else {
	  cout << "wrong \n";
	}
  }

  return 0;
}