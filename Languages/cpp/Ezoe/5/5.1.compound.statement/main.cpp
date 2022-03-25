#include "../../all.hpp"

int main() {
  {
    std::cout << "hello\n"s;
    std::cout << "hello\n"s;
  }

  auto a = 12345 + 6789;
  auto b = 073 * 132 / 5;
  if (a > b) {
    std::cout << "b = "s << b;
  } else {
    std::cout << "a = "s << a;
  }
}
