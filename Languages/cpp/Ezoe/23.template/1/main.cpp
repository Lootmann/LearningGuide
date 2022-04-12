#include "../../all.hpp"

template <typename T>
T twice(T n) {
  std::cout << typeid(n).name() << "\n"s;
  return n * 2;
}

auto print = [](auto n) {
  std::cout << n << "\n"s;
};

template <typename T>
void f(T const &x) {
  std::cout << x << "\n"s;
}

int main() {
  print(twice(123));
  print(twice(1.23));

  f<int>(0);
  f<long int>(1);
  f<long long int>(2);
  f<double>(3);
}
