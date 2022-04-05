#include "../../all.hpp"

// x is reference
void f(int &x) {
  x = 3;
}

void swap(int &a, int &b) {
  auto temp = a;
  a = b;
  b = temp;
}

void print(int x) {
  std::cout << x << "\n"s;
}

void print(int x, int y) {
  std::cout << x << " " << y << "\n"s;
}

void g(std::vector<int> const &v) {
  std::cout << "size = " << v.size() << "\n"s;
}

int main() {
  int a = 1;
  int b = 2;

  // lvalue reference
  int &ref = a;
  print(ref);

  f(ref);

  print(ref);

  // const
  const int &const_ref = a;
  int const &const_ref1 = b;
  print(a, b);

  std::vector<int> v(10000);
  g(v);
}
