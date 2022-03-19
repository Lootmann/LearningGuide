#ifndef INCLUDE_GUARD_ARRAY_STACK_HPP
#define INCLUDE_GUARD_ARRAY_STACK_HPP

#include <iostream>

#include "./array.hpp"

template <typename T>
class ArrayStack {
private:
  Array<T> arr;
  std::size_t index;

public:
  ArrayStack() : arr(0), index(0) {}

  void push(T elem) {
    if (index + 1 >= arr.size()) arr.resize();
    arr[index++] = elem;
  }

  T pop() {
    if (arr.size() >= 3 * index) arr.resize();
    T popped = arr[--index];
    return popped;
  }

  T top() {
    return arr[index - 1];
  }

  bool empty() {
    return index == 0;
  }

  std::size_t size() const {
    return index;
  }
};

#endif /* INCLUDE_GUARD_ARRAY_STACK_HPP */