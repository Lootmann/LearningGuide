#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

// linear
void solve() {
  for (int up = 20; up <= 99; ++up) {
    for (int bottom = 10; bottom <= 99; ++bottom) {
      // first
      int first = up * (bottom % 10);

      // second
      int second = up * (bottom / 10);

      if ((100 <= first && first <= 999) && (first / 10 % 10 == 3) &&
          (10 <= bottom && bottom <= 99)) {
        int answer = first + second * 10;

        if ((100 <= answer && answer <= 999) && answer / 10 % 10 == 4) {
          cout << "=== ans ===" << '\n';
          cout << " " << up << '\n';
          cout << "x" << bottom << '\n';
          cout << "---" << '\n';
          cout << first << '\n';
          cout << second << '\n';
          cout << "---" << '\n';
          cout << answer << '\n';
          cout << "\n\n";
        }
      }
    }
  }
}

int main() {
  FastIO;
  solve();
}
