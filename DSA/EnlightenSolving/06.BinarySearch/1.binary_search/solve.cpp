#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

int binary_search(int key, vector<int> const &A) {
  int left = 0;
  int right = (int)A.size() - 1;

  while (right >= left) {
    int mid = (left + right) / 2;

    if (A[mid] == key) {
      return mid;
    } else if (A[mid] < key) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
}

int main() {
  FastIO;

  int n;
  cin >> n;

  vector<int> A(n);
  for (auto &a : A) cin >> a;

  vector<int> tests{10, 3, 39, -100, 9, 100};
  for (int test : tests) {
    cout << setw(4) << test;
    cout << ' ' << binary_search(test, A) << '\n';
  }
}
