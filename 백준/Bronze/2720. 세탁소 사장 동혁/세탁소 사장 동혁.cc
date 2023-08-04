#include <bits/stdc++.h>
using namespace std;

int T, paymoney;

int main() {
    cin >> T;
    while (T--) {
        int Q = 0, D = 0, N = 0, P = 0;
        cin >> paymoney;
        while(paymoney) {
            if(paymoney >= 25) {
                Q++;
                paymoney -= 25;
            } else if(paymoney >= 10) {
                D++;
                paymoney -= 10;
            } else if(paymoney >= 5) {
                N++;
                paymoney -= 5;
            } else {
                P++;
                paymoney -= 1;
            }
        }
        cout << Q << " " << D << " " << N << " " << P << "\n";
    }
}