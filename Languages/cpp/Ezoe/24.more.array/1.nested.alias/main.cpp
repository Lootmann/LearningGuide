#include "../../all.hpp"

template <typename T, std::size_t N>
struct Array {
  using value_type = T;
  using reference = T &;
  using const_reference = T const &;
  using size_type = std::size_t;

  value_type storage[N];

  reference operator[](size_type i) {
    return storage[i];
  }

  // can't change cause const
  const_reference operator[](size_type i) const {
    return storage[i];
  }

  size_type size() const {
    return N;
  }
};
template <typename Array>
void print(Array const &c) {
  for (std::size_t i = 0; i < c.size(); ++i) {
    std::cout << c[i];
  }
}

int main() {
  Array<int, 5> a = {1, 2, 3, 4, 5};

  print(a);
}
