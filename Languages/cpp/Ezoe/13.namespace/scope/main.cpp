#include "../../all.hpp"

auto f = []() {
  std::cout << 1;
};

int main() {
  f();

  auto f = []() {
    std::cout << 2;
  };

  f();

  {
    f();

    auto f = []() {
      std::cout << 3;
    };
    f();
  }
  f();
}
