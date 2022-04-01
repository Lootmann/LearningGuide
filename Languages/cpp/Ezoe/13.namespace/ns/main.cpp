#include "../../all.hpp"

namespace ns {
int name{};

int f() {
  return 0;
}
}  // namespace ns

int f() {
  return ns::name;
}

namespace b {
int f() {
  return 1;
}
}  // namespace b

namespace A {
namespace B {
namespace C {
std::string name{"greeting"};

}  // namespace C
}  // namespace B
}  // namespace A

namespace very_long_alias_namespace_collapse_name {
int f() {
  return 0;
}
}  // namespace very_long_alias_namespace_collapse_name

auto print = [](auto x) {
  std::cout << x << "\n"s;
};

int x{};

int main() {
  ns::name = 1;

  print(ns::name);

  // dont collision
  print(ns::f());
  print(b::f());

  print(x);
  print(::x);

  print(A::B::C::name);

  namespace vln = very_long_alias_namespace_collapse_name;
  print(vln::f());
}
