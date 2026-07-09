#include <string>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int solution(int n) {
    vector<int> is_prime(n + 1, 1);
    is_prime[0]=0;
    is_prime[1]=0;

    for (int i=2; i*i<=n; i++) {
        if (is_prime[i]) {
            for (int j=i; j*i<=n; j++) {
                is_prime[j*i] = 0;
            }
        }
    }

    int answer = accumulate(is_prime.begin(), is_prime.end(), 0);
    return answer;
}