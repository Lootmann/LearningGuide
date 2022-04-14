#include "../../all.hpp"

auto p = [](auto x) {
  std::cout << x << "\n"s;
};

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

  // front()
  reference front() {
    return storage[0];
  }

  const_reference front() const {
    return storage[0];
  }

  // back()
  reference back() {
    return storage[N - 1];
  }

  const_reference back() const {
    return storage[N - 1];
  }

  void fill(T const &u) {
    for (std::size_t i = 0; i != N; ++i) {
      storage[i] = u;
    }
  }

  // size
  size_type size() const {
    return N;
  }
};

template <typename Array>
void print(Array const &c) {
  for (std::size_t i = 0; i < c.size(); ++i) {
    std::cout << c[i] << " "s;
  }
  std::cout << "\n"s;
}

int main() {
  Array<int, 5> a = {1, 2, 3, 4, 5};
  print(a);

  a.fill(9);
  print(a);

  int f = a.front();
  int const cf = a.front();

  p(f);
  p(cf);
}
