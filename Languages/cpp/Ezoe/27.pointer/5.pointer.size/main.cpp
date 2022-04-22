#include "../../all.hpp"

template <typename T>
void print_size() {
  std::cout << sizeof(T) << "\n"s;
}

void *memcpy(void *dest, void const *src, std::size_t n) {
  auto d = static_cast<std::byte *>(dest);
  auto s = static_cast<std::byte const *>(src);

  auto last = s + n;

  while (s != last) {
    *d = *s;
    ++d;
    ++s;
  }

  return dest;
}

template <typename To, typename From>
To bit_cast(From const &from) {
  To to;
  memcpy(&to, &from, sizeof(To));
  return to;
}

template <typename T>
void print_raw_addresS(T ptr) {
  std::cout << bit_cast<std::uintptr_t>(ptr) << "\n"s;
}

struct Object {
  int x = 123;
  int y = 456;
  int z = 789;
};

int main() {
  print_size<int *>();
  print_size<double *>();
  print_size<int **>();
  print_size<std::uintptr_t>();
  print_size<int>();

  int data[]{0, 1, 2, 3, 4};
  int *ptr = &data[0];
  std::cout << ptr << "\n"s;
  ptr++;
  std::cout << ptr << "\n"s;

  Object object;
  std::byte *start = bit_cast<std::byte *>(&object);
  int *x = bit_cast<int *>(start + 0);
  int *y = bit_cast<int *>(start + 4);
  int *z = bit_cast<int *>(start + 8);
  std::cout << *x << *y << *z;
}
