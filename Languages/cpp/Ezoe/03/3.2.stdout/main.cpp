#include "../../all.hpp"

int main() {
  std::cout << "one"s;
  std::cout << "two"s;
  std::cout << "three"s;

  std::cout << "aaa\nbbb\nccc\n"s;
  std::cout << "hello"s + " "s + "world\n"s;
  std::cout << 1 + 123 << "\n";
  // std::cout << 1 + "234";

  // variable init
  auto a = 1;
  auto b(2);
  auto c{3};

  int i = 1;
  double d = 1.23;
  std::string s = "123"s;
}
