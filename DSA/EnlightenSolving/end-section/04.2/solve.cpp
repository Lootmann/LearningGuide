#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

long long trib(long long n, vector<long long int> &memos) {
  // base cases
  if (n < 0) return 0;
  if (n == 0 || n == 1 || n == 2) return memos[n];

  // return cache
  if (memos[n] != 0) return memos[n];
  // cached
  return memos[n] = memos[n - 1] + memos[n - 2] + memos[n - 3];
}

int main() {
  FastIO;

  vector<long long int> memos(50);
  memos.assign(50, 0);
  memos[0] = 0;
  memos[1] = 0;
  memos[2] = 1;

  for (int i = 0; i < 50; ++i) {
    trib(i, memos);
  }

  for (int i = 0; i < 50; ++i) {
    cout << i << ' ' << memos[i] << '\n';
  }
}
