#ifndef INCLUDE_GUARD_ARRAY_HPP
#define INCLUDE_GUARD_ARRAY_HPP

#include <algorithm>
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

  ~Array() {
    delete[] a;
  }

  std::size_t size() const {
    return length;
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

  void resize() {
    std::size_t new_size = std::max(2 * length, static_cast<std::size_t>(1));
    T* new_arr = new T[new_size];
    for (std::size_t i = 0; i < length; ++i) {
      new_arr[i] = a[i];
    }
    a = new_arr;
    length = new_size;
  }
};

#endif /* INCLUDE_GUARD_ARRAY_HPP */