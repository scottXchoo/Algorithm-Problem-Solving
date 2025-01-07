#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int sum = 0;
    vector<int> inputs(5);

    for (int i = 0; i < 5; i++) {
        cin >> inputs[i];
        sum += inputs[i];
    }

    sort(inputs.begin(), inputs.end());

    cout << sum / 5 << endl << inputs[5 / 2] << endl;

    return 0;
}