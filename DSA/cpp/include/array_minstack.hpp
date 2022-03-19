#ifndef INCLUDE_GUARD_ARRAY_MINSTACK
#define INCLUDE_GUARD_ARRAY_MINSTACK

#include <algorithm>

template <typename T>
class MinNode {
public:
  T data, min;
};

template <typename T>
class ArrayMinStack {
private:
  std::size_t index, length;
  MinNode<T>* arr;

public:
  using Type = MinNode<T>;

  ArrayMinStack() : index(0), length(0) {
    arr = new Type[length];
  }

  void push(T elem) {
    if (index + 1 >= length) this->resize();

    arr[index].data = elem;
    arr[index].min = (index == 0 ? elem : std::min(arr[index - 1].min, elem));
    index++;
  }

  Type pop() {
    if (length >= 3 * index) resize();
    return arr[--index];
  }

  T top() {
    return arr[index - 1].data;
  }

  T min() {
    return arr[index - 1].min;
  }

  bool empty() {
    return index == 0;
  }

  void resize() {
    std::size_t new_size = std::max(2 * length, static_cast<std::size_t>(1));

    Type* new_arr = new Type[new_size];
    for (std::size_t i = 0; i < length; ++i) {
      new_arr[i] = arr[i];
    }
    arr = new_arr;
    length = new_size;
  }

  std::size_t size() const {
    return index;
  }
};

#endif /* INCLUDE_GUARD_ARRAY_MINSTACK */
