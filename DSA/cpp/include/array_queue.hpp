#ifndef INCLUDE_GUARD_ARRAY_QUEUE_HPP
#define INCLUDE_GUARD_ARRAY_QUEUE_HPP

#include <algorithm>
#include <iostream>

#include "./array.hpp"

template <typename T>
class ArrayQueue {
private:
  Array<T> arr;
  std::size_t index_, size_;

public:
  ArrayQueue() : arr(0), index_(0), size_(0) {}

  void enqueue(T elem) {
    if (size_ + 1 >= arr.size()) resize();
    arr[(index_ + size_) % arr.size()] = elem;
    size_++;
  }

  T dequeue() {
    T x = arr[index_];
    index_ = (index_ + 1) % arr.size();
    size_--;
    if (arr.size() >= 3 * size_) resize();
    return x;
  }

  T front() {
    return arr[index_];
  }

  bool empty() {
    return size_ == 0;
  }

  void resize() {
    Array<T> b(std::max(2 * size_, static_cast<std::size_t>(1)));
    for (std::size_t i = 0; i < size_; ++i) {
      b[i] = arr[(index_ + i) % arr.size()];
    }
    arr = b;
    index_ = 0;
  }

  std::size_t size() const {
    return size_;
  }
};

#endif /* INCLUDE_GUARD_ARRAY_QUEUE_HPP */