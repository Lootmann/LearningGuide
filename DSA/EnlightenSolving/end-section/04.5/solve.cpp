#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;
using llint = long long int;

bool include(const string& str) {
  bool is_3 = false, is_5 = false, is_7 = false;
  for (auto ch : str) {
    if (ch == '3') is_3 = true;
    if (ch == '5') is_5 = true;
    if (ch == '7') is_7 = true;
  }

  return is_3 && is_5 && is_7;
}

void celebrate(string str, llint K, llint& count) {
  // base
  if (str != "" && K < stoll(str)) return;

  // include 3, 5, 7
  if (include(str)) count++;

  celebrate("7" + str, K, count);
  celebrate("5" + str, K, count);
  celebrate("3" + str, K, count);
}

int main() {
  FastIO;

  llint K;
  cin >> K;

  llint count = 0;
  celebrate("", K, count);
  cout << count << '\n';
}
