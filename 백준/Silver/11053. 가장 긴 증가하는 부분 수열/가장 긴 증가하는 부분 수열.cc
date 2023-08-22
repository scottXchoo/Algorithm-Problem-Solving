#include <bits/stdc++.h>
using namespace std;

int n, a[1001], cnt[1001], ret;

int main() {
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        scanf("%d", a + i);
    }
    
    for(int i = 0; i < n; i++) {
        int maxValue = 0;
        for(int j = 0; j < i; j++) {
            if(a[j] < a[i] && maxValue < cnt[j]) maxValue = cnt[j];
        }
        cnt[i] = maxValue + 1;
        ret = max(ret, cnt[i]);
    }
    printf("%d\n", ret);
}