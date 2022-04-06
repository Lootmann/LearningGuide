#include "../all.hpp"

int main() {
  auto f = [](bool x) -> int {
    if (x) return 0;
    return 1;
  };

  int n = f(true);
  int m = f(false);

  std::cout << n << " " << m << "\n"s;

  std::string str = "std::string str";

  // copy capture
  [=]() {
    std::cout << str << "\n"s;
  }();

  // reference capture
  auto g = [&]() {
    str = "change";
  };
  g();

  std::cout << str << "\n"s;
}
