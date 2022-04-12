#include "../../all.hpp"

template <typename T, T N>
T value() {
  return N;
}

auto print = [](auto x) {
  std::cout << x << '\n';
};

template <typename T, std::size_t N>
struct array {
  T storage[N];

  T &operator[](std::size_t i) {
    return storage[i];
  }
};

int main() {
  auto n = value<int, 1>();
  auto m = value<short, 1>();

  print(n);
  print(m);
}