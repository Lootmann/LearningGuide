#include "../../all.hpp"

struct Object {
  int sub;

  void m_func() {
    std::cout << sub << "\n"s;
  }
};

struct C {
  int f(int) {
    return 0;
  }
};

auto print = [](auto x) {
  std::cout << x << "\n"s;
};

int main() {
  Object obj;
  int *pointer = &obj.sub;

  *pointer = 123;
  int read = obj.sub;

  print(read);

  int Object::*int_ptr = &Object::sub;
  std::cout << int_ptr << "\n"s;
}
