#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int get_primes(int n) {
    int count = 0;
    if (n < 2) return 0;
    
    vector<int> is_prime(n+1, 1);
    
    is_prime[0] = is_prime[1] = 0;
    
    for (int i = 2; i * i <= n; i++) {   
        if (!is_prime[i]) continue;
        
        for (int j = i * i; j <= n; j += i) {
            is_prime[j] = false;
        }
    }
    
    for (int i = 2; i <= n; i++) {
        if (is_prime[i]) {
            count++;
        }
    }
    return count;
}

int solution(int n) {
    cin >> n;
    int answer = get_primes(n);
    return answer;
}