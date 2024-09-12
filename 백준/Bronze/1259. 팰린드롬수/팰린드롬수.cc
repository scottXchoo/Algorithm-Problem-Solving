#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
  string N;

  while (N != "0") {
	cin >> N;
	string temp = N;
	reverse(N.begin(), N.end());
	if (N == "0") break;

	if (N == temp) {
	  cout << "yes \n";
	} else {
	  cout << "no \n";
	}
  }

  return 0;
}