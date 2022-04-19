#include "../../all.hpp"

int f(int x) {
  std::cout << x;
  return x;
}

int main() {
  using f_type = int(int);
  using f_ptr = f_type *;

  f_ptr ptr = &f;

  (*ptr)(123);
}
