#include "../../all.hpp"

using std::cout;

auto print = [](auto x) {
  cout << sizeof(x) << '\n';
};

int main() {
  int n = 1;
  print(n);

  long int li = 2;
  long long int lli = 3;
  unsigned long long ull = 4;

  print(li);
  print(lli);
  print(ull);
}
