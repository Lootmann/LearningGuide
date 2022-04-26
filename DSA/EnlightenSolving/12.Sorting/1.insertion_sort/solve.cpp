#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

void InsertionSort(vector<int> &a) {
  int N = (int)a.size();

  for (int i = 1; i < N; ++i) {
    int v = a[i];

    int j = i;
    for (; j > 0; --j) {
      if (a[j - 1] > v) {
        a[j] = a[j - 1];
      } else
        break;
    }
    a[j] = v;
  }
}

auto print = [](auto &A) {
  for (auto a : A) cout << a << ' ';
  cout << "\n";
};

int main() {
  FastIO;

  int N;
  cin >> N;
  vector<int> A(N);
  for (auto &a : A) cin >> a;

  print(A);
  InsertionSort(A);
  print(A);
}
