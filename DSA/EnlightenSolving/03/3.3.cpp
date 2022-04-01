// get min value from input file
#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

int main() {
  FastIO;
  int n, v;
  cin >> n >> v;

  vector<int> a(n);

  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }

  // min value
  int min_value = 20000000;

  for (int i = 0; i < n; ++i) {
    if (a[i] < min_value) min_value = a[i];
  }

  cout << min_value << '\n';
}
