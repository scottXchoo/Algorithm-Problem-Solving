#include <iostream>
#include <set>

using namespace std;

int main() {
    int A, B;
    cin >> A >> B;

    set<int> Aset, Bset, Aans, Bans;

    for (int i = 0; i < A; i++) {
        int value;
        cin >> value;
        Aset.insert(value);
        Aans.insert(value);
    }

    for (int i = 0; i < B; i++) {
        int value;
        cin >> value;
        Bset.insert(value);
        Bans.insert(value);
    }

    int ans = 0;
    for (auto i : Bset) {
        Aans.erase(i);
    }
    for (auto i : Aset) {
        Bans.erase(i);
    }

    cout << Aans.size() + Bans.size() << '\n';

    return 0;
}