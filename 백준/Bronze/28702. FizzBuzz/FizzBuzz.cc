#include <iostream>
#include <string>

using namespace std;

int main() {
  string answer;
  for (int i = 0; i < 3; i++) {
	string str;
	cin >> str;

	if (str[0] == 'F' || str[0] == 'B') continue;

	int num = stoi(str) + 3 - i;

	if (num % 3 == 0 && num % 5 == 0) {
	  answer = "FizzBuzz";
	  break;
	} else if (num % 3 == 0 && num % 5 != 0) {
	  answer = "Fizz";
	  break;
	} else if (num % 3 != 0 && num % 5 == 0) {
	  answer = "Buzz";
	  break;
	} else {
	  answer = to_string(num);
	  break;
	}
  }

  cout << answer;

  return 0;
}