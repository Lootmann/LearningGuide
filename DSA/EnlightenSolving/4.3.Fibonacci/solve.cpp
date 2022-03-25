#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int fibonacci(int n) {
  cout << "call fibonacci(" << n << ")\n";
  if (n == 0) return 0;
  if (n == 1) return 1;

  int result = fibonacci(n - 1) + fibonacci(n - 2);
  cout << n << " = " << result << '\n';
  return result;
}

int main() {
  FastIO;

  vector<int> nums{};
  for (int i = 1; i <= 10; ++i) {
    nums.emplace_back(i);
  }

  for (auto num : nums) {
    cout << num << " " << fibonacci(num) << '\n';
  }
}
