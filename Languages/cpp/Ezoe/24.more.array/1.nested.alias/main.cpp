#include "../../all.hpp"

template <typename T, std::size_t N>
struct array {
  using value_type = T;
  using reference = T&;

  using size_type = std::size_t;

  value_type storage[N];

  reference operator[](size_type i) {
    return storage[i];
  }
};

struct S {
  using number = int;
  number data;
};

auto print = [](auto x) {
  std::cout << x << "\n"s;
};

int main() {
  using number = int;
  number x = 123;

  print(x);

  S s{123};
  S::number y = s.data;
  print(y);
}
