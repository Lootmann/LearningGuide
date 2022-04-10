#include "../../all.hpp"

struct Point {
  int x = 0;
  int y = 0;
};

struct Person {
  std::string name;
  int age;
};

struct Fractional {
  int num;
  int denom;

  double value() {
    return static_cast<double>(num) / static_cast<double>(denom);
  }
};

auto info = [](Person person) {
  std::cout << person.name << " "s << person.age << "\n";
};

int main() {
  Point p;
  std::cout << p.x << " "s << p.y << "\n"s;

  Person me;
  me.name = "lyota";
  me.age = 35;
  info(me);

  Fractional f{1, 2};
  std::cout << f.value() << "\n"s;
}
