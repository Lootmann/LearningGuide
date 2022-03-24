#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define NOT_FOUND -1
using namespace std;

int main() {
  FastIO;

  int n, v;
  cin >> n >> v;

  vector<int> a(n);
  rep(i, n) cin >> a[i];

  int found_id = NOT_FOUND;

  for (int i = 0; i < n; ++i) {
    if (a[i] == v) {
      found_id = i;
    }
  }

  if (found_id == NOT_FOUND)
    cout << "Not Found" << '\n';
  else
    cout << found_id << '\n';
}
