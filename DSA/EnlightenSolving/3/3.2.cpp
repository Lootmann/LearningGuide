// get array id
#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

const int NOT_FOUND = -1;

int main() {
  FastIO;
  int n, v;
  cin >> n >> v;

  vector<int> a(n);

  // O(n)
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }

  // flag
  int found_id = NOT_FOUND;

  // O(n)
  for (int i = 0; i < n; ++i) {
    if (a[i] == v) found_id = i;
  }

  if (found_id == NOT_FOUND)
    cout << "Not Found :^)" << '\n';
  else
    cout << found_id << '\n';
}
