#include "../../all.hpp"

int plus(int x, int y) {
  return x + y;
}

double plus(double x, double y) {
  return x + y;
}

std::string plus(std::string x, std::string y) {
  return x + y;
}

auto print = [](auto x) {
  std::cout << x << "\n"s;
};

int main() {
  auto i = plus(1, 2);
  auto d = plus(1.2, 3.4);
  auto s = plus("hello"s, "world"s);

  print(i);
  print(d);
  print(s);
}
