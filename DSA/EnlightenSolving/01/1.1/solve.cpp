#include <bits/stdc++.h>
#define FastIO cin.tie(nullptr), ios_base::sync_with_stdio(false);
using namespace std;

int linear(int year) {
  int count{};
  for (int i = 20; i < 36; ++i) {
    count++;
    if (year == i) {
      return count;
    }
  }

  return count;
}

int binary_search(int year) {
  int low = 20, high = 35, count = 0;

  while (low <= high) {
    int mid = (low + high) / 2;
    if (mid == year) {
      break;
    } else if (mid > year) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
    count++;
  }

  return count;
}

int get_year(int min, int max) {
  std::random_device rnd;
  std::mt19937 mt(rnd());
  mt.seed(rnd());
  std::uniform_int_distribution<> rand_year(min, max);
  return rand_year(mt);
}

int main() {
  FastIO;
  int year = get_year(20, 36);
  cout << "linear result = " << linear(year) << '\n';
  cout << "binary search result = " << binary_search(year) << '\n';
}
