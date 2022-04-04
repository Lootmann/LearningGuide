#include "../../all.hpp"

auto print = [](auto x) {
  std::cout << x << "\n"s;
};

int main() {
  1 + 1;  // expression
  1 < 2;  // expression

  std::cout << std::boolalpha;
  print(1 == 1);
  print(1 != 1);

  if (true) {
    print("true");
  } else {
    print("false");
  }

  print("-- logical operator --");
  print(true && true);
  print(true && false);
  print(false && true);
  print(false && false);

  print("-- logical operator --");
  print(true || true);
  print(true || false);
  print(false || true);
  print(false || false);

  print("-- short circuit --");
  auto a = []() {
    std::cout << "a\n"s;
    return false;
  };

  auto b = []() {
    std::cout << "b\n"s;
    return true;
  };

  bool c = a() && b();
  std::cout << c << "\n"s;
  std::cout << (a() && b()) << "\n"s;
}
