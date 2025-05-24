#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<int> answer_v;
vector<string> max_v;
vector<int> min_v;

string input;

string find_max() {
    stack<char> st;
    string temp;
    for (const char i : input) {
        if (st.empty()) {
            if (i == 'K') {
                temp.append(to_string(5));
            } else if (i == 'M') {
                st.push(i);
            }
        } else { // i == 'M'
            if (st.top() == 'M' && i == 'K') {
                temp.append(to_string(5));
                for (int j = 0; j < st.size(); j++) {
                    temp.append(to_string(0));
                }

                // Stack 비우기
                while (!st.empty()) {
                    st.pop();
                }
            } else {
                st.push(i);
            }
        }
    }

    if (!st.empty()) {
        for (int i = 0; i < st.size(); i++) {
            temp.append(to_string(1));
        }
    }

    return temp;
}

string find_min() {
    vector<char> M;
    string temp;
    for (const char i : input) {
        // K가 있을 때까지 Cut
        if (i == 'K') {
            if (!M.empty()) {
                temp.append(to_string(1));
                for (int j = 0; j < M.size() - 1; j++) {
                    temp.append(to_string(0));
                }

                temp.append(to_string(5));
                M.clear();
            } else if (M.empty()) {
                temp.append(to_string(5));
            }
        } else if (i == 'M') {
            M.push_back('M');
        }
    }

    // K가 없고 계속 M이면, 이렇게 처리
    if (!M.empty()) {
        temp.append(to_string(1));
        for (int j = 0; j < M.size() - 1; j++) {
            temp.append(to_string(0));
        }
    }

    return temp;
}

int main() {
    cin >> input;
    cout << find_max() << '\n';
    cout << find_min();

    return 0;
}