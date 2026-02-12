#include <iostream>
#include <queue>

using namespace std;

const int INF = 1e9;
int N = 0;

int main() {
    cin >> N;

    vector<int> days(N+1, INF);
    vector<int> waters(N+1, INF);

    days[0] = 0;
    waters[0] = 0;

    queue<int> q;
    q.push(0);

    while (!q.empty()) {
        int c_len = q.front();
        q.pop();

        int n_day = days[c_len] + 1;

        // 1. c_len + 1
        if (c_len + 1 <= N) {
            int n_len = c_len + 1;
            int n_water = waters[c_len] + 1;

            if (days[n_len] > n_day) {
                days[n_len] = n_day;
                waters[n_len] = n_water;
                q.push(n_len);
            } else if (days[n_len] == n_day && waters[n_len] > n_water) {
                waters[n_len] = n_water;
                q.push(n_len);
            }
        }

        // 2. c_len * 3
        if (c_len * 3 <= N) {
            int n_len = c_len * 3;
            int n_water = waters[c_len] + 3;

            if (days[n_len] > n_day) {
                days[n_len] = n_day;
                waters[n_len] = n_water;
                q.push(n_len);
            } else if (days[n_len] == n_day && waters[n_len] > n_water) {
                waters[n_len] = n_water;
                q.push(n_len);
            }
        }

        // 3. c_len ** c_len
        if ((long long)c_len * c_len <= N) {
            int n_len = c_len * c_len;
            int n_water = waters[c_len] + 5;

            if (days[n_len] > n_day) {
                days[n_len] = n_day;
                waters[n_len] = n_water;
                q.push(n_len);
            } else if (days[n_len] == n_day && waters[n_len] > n_water) {
                waters[n_len] = n_water;
                q.push(n_len);
            }
        }
    }

    cout << days[N] << " " << waters[N] << "\n";

    return 0;
}