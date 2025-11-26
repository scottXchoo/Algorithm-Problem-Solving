#include <iostream>
#include <algorithm>
#define MAX 1000005
using namespace std;
typedef long long ll;

ll N, M, answer;
int trees[MAX];

void input() {
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        cin >> trees[i];
    }
}

int main() {
    input();

    sort(trees, trees + N);
    ll low = 0;
    ll high = trees[N-1];

    while (low <= high) {
        ll sum = 0;
        ll cut = (low + high) / 2;

        for (int i = 0; i < N; i++) {
            if (trees[i] - cut > 0) sum += trees[i] - cut;
        }

        if (sum >= M) {
            answer = cut;
            low = cut + 1;
        } else {
            high = cut - 1;
        }
    }
    cout << answer;

    return 0;
}