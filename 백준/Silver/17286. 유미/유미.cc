#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

struct Point {
    int x, y;
};

double calcDist(const Point &a, const Point &b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

int main() {
    Point yumi;
    cin >> yumi.x >> yumi.y;

    vector<Point> persons(3);
    for (int i = 0; i < 3; i++) {
        cin >> persons[i].x >> persons[i].y;
    }

    vector<int> perm;
    perm.push_back(0);
    perm.push_back(1);
    perm.push_back(2);

    double minDistance = 1e9;

    do {
        double distSum = 0.0;
        distSum += calcDist(yumi, persons[perm[0]]);
        distSum += calcDist(persons[perm[0]], persons[perm[1]]);
        distSum += calcDist(persons[perm[1]], persons[perm[2]]);

        if (distSum < minDistance) {
            minDistance = distSum;
        }
    } while (next_permutation(perm.begin(), perm.end()));

    cout << static_cast<int>(minDistance) << "\n";

    return 0;
}