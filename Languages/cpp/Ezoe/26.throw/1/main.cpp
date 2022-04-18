#include "../../all.hpp"

struct Object {
  std::string name;

  Object(std::string const& name) : name(name) {
    std::cout << name << " is constructed.\n"s;
  }

  ~Object() {
    std::cout << name << " is destructed.\n"s;
  }
};

int main() {
  {
    // hello
    Object obj("obj"s);
  }
  std::out_of_range err("I am error");
  std::cout << err.what();
}
