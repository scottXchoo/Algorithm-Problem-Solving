#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N;
    double sum = 0;
    double drinks[100001];
    double max;

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> drinks[i];
        sum += drinks[i];
    }

    sort(drinks, drinks + N);
    max = drinks[N-1];
    
    double ans = (sum - max) / 2 + max;
    cout << ans;

    return 0;
}