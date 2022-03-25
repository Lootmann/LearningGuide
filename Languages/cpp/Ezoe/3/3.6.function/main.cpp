#include "../../all.hpp"

int main() {
  /*
    [] : capture list
    () : parameter list
    {} : function body
  */
  auto print = [](auto x) {
    std::cout << x << "\n"s;
  };

  auto twice = [](auto x) {
    std::cout << x << " "s << x << "\n"s;
  };

  print(123);
  print(3.14);
  print("hello");

  twice("hello world");

  // empty lambda
  auto func = []() {};
  func();

  // IIFE
  []() {}();
}
