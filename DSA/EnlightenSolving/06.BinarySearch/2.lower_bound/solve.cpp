#include <bits/stdc++.h>
using namespace std;

bool is_ok(int x) {
  return x >= 28;
}

// lower_bound
int binary_search(int ng, int ok) {
  cout << "ng  ok  [mid]" << '\n';

  while (abs(ok - ng) > 1) {
    int mid = (ok + ng) / 2;
    cout << ng << "  " << ok << "  [" << mid << "]" << '\n';

    if (is_ok(mid))
      ok = mid;
    else
      ng = mid;
  }

  return ok;
}

int main() {
  int ng = -1, ok = 100;
  cout << binary_search(ng, ok) << '\n';
}
