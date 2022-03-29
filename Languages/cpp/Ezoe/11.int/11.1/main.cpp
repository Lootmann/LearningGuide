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
}
