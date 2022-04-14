#include "../../all.hpp"

struct S {
  int data{};

  int &get() {
    std::cout << "&get()\n"s;
    return data;
  }

  int const &get() const {
    std::cout << "const &get()\n"s;
    return data;
  }

  int f() {
    std::cout << "f()\n"s;
    return data;
  }

  int f() const {
    std::cout << "f() const\n"s;
    return data + 1;
  }
};

auto p = [](auto x) {
  std::cout << x << "\n"s;
};

int main() {
  S s;
  p(s.f());

  int num = s.get();
  p(num);

  num = 10;
  p(num);

  int const n = s.get();
  p(n);

  S const cs;
  p(cs.f());
}
