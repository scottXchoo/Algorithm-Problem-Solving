#include <bits/stdc++.h>
using namespace std;

int n = 3;
int k = 2;

void print(vector<int> b)
{
    for (int i : b)
        cout << i << " ";
    cout << '\n';
}
void combi(int start, vector<int> b)
{
    cout << n << " : " << k << "\n";
    if (b.size() == k)
    {
        // logic
        print(b);
        return;
    }
    for (int i = start + 1; i < n; i++)
    {
        b.push_back(i);
        combi(i, b);
        b.pop_back();
    }
    return;
}

int main()
{
    vector<int> b;
    combi(-1, b);
    return 0;
}