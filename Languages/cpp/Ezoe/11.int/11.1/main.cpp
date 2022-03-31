#include "../../all.hpp"

auto print = [](auto x) {
  std::cout << x << "\n"s;
};

int main() {
  int a = 123;
  int decimal = 123;
  int octal = 0123;
  int binary = 0b1010;
  int hex = 0x123;
  int hex_c = 0xFF;

  print(a);
  print(decimal);
  print(octal);
  print(binary);
  print(hex);
  print(hex_c);

  int x = 123;
  int y = 123u;
  print(x);
  print(y);

  auto long_num = 100'0000'0000;
  print(long_num);

  print(sizeof(std::size_t));
  print(sizeof(long));
  print(sizeof(long long));
  print(sizeof(unsigned long long));

  print(std::numeric_limits<int>::max());
  print(std::numeric_limits<int>::min());

  print(std::numeric_limits<int>::max());
  print(std::numeric_limits<int>::min());

  print(std::numeric_limits<unsigned long long>::max());
  print(std::numeric_limits<unsigned long long>::min());
}
