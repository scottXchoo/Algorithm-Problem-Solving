#include <bits/stdc++.h>
using namespace std;

// #1
int main()
{
	int a[] = {1, 2, 3};
	do
	{
		for (int i : a)
			cout << i << " ";
		cout << '\n';
	} while (next_permutation(&a[0], &a[0] + 3));
}

// #2
int main()
{
	// 반드시 오름차순 이어야 됨
	vector<int> a{2, 1, 3};
	sort(a.begin(), a.end());
	do
	{
		for (int i : a)
			cout << i << " ";
		cout << '\n';
	} while (next_permutation(a.begin(), a.end()));
}