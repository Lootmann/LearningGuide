#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

long long fibo_memo(vector<long long>& memo, int n) {
  if (n == 0) return 0;
  if (n == 1) return 1;

  // check whether memo[n] is cached
  if (memo[n] != -1) return memo[n];
  return memo[n] = fibo_memo(memo, n - 1) + fibo_memo(memo, n - 2);
}

int main() {
  FastIO;

  // memorization
  vector<long long> memo;
  memo.assign(50, -1);

  fibo_memo(memo, 49);

  for (int i = 0; i < 50; ++i) {
    cout << i << " " << memo[i] << '\n';
  }
}
