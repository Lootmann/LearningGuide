#include "../../all.hpp"

auto BMI = [](auto height, auto mass) {
  return mass / (height * height);
};

int main() {
  double height{};
  double mass{};

  std::cin >> height >> mass;
  double bmi = BMI(height, mass);
  std::cout << "BMI = "s << bmi << "\n"s;
}
