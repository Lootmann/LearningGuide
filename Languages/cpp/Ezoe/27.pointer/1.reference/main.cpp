#include "../../all.hpp"

auto print = [](auto x) {
  std::cout << x << "\n"s;
};

int main() {
  int objects = 0;
  objects = 123;
  print(objects);

  int& reference = objects;
  reference = 456;

  // reference
  int m = 0;
  int& rm = m;
  print(rm);

  // pointer
  int n = 0;
  int* pn = &n;
  print(*pn);

  const int x{};
  const int* px = &x;

  const int nn{};
  const int& rnn = nn;
}
