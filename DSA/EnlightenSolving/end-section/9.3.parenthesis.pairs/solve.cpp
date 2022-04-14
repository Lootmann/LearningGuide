#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

bool is_open_bracket(char ch) {
  return ch == '(' || ch == '{' || ch == '[';
}

struct bracket_pair {
  char bracket;
  int index;
};

void solve() {
  string str;
  cin >> str;

  vector<bracket_pair> ans;
  stack<bracket_pair> st;

  for (int i = 0; i < (int)str.size(); ++i) {
    auto ch = str[i];

    if (is_open_bracket(ch)) {
      auto bp = bracket_pair{ch, i};
      st.push(bp);
      ans.emplace_back(bp);
    } else {
      if (st.empty()) {
        cout << "Not Enough\n";
        return;
      }

      auto pop = st.top();
      st.pop();

      bool is_match = pop.bracket == '(' && ch == ')';
      is_match |= pop.bracket == '{' && ch == '}';
      is_match |= pop.bracket == '[' && ch == ']';

      if (!is_match) {
        cout << "Not Match\n";
        return;
      }

      ans.emplace_back(bracket_pair{ch, pop.index});
    }
  }  // for

  for (auto a : ans) {
    cout << a.bracket << " (" << a.index << ")\n";
  }
}

int main() {
  FastIO;
  int n;
  cin >> n;

  rep(i, n) {
    cout << "TEST " << i + 1 << "\n"s;
    solve();
    cout << '\n';
  }
}
