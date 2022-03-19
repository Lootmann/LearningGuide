#ifndef INCLUDE_GUARD_ARRAY_HPP
#define INCLUDE_GUARD_ARRAY_HPP

#include <cassert>
#include <iostream>

template <typename T>
class Array {
private:
  T* a;
  std::size_t length;

public:
  Array(std::size_t length) : length(length) {
    a = new T[length];
  }

  T& operator[](std::size_t i) {
    assert(0 <= i && i < length);
    return a[i];
  }

  Array<T>& operator=(Array<T>& b) {
    if (a != nullptr) delete[] a;
    a = b.a;
    b.a = nullptr;
    length = b.length;
    return *this;
  }

  void Fill() {
    for (std::size_t i = 0; i < length; ++i) {
      a[i] = T();
    }
  }

  std::size_t size() const {
    return length;
  }
};

#endif /* INCLUDE_GUARD_ARRAY_HPP */