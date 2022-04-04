#include "../../all.hpp"

auto status = [](double bmi) {
  if (bmi < 18.5)
    return "Underweight.\n"s;
  else if (bmi < 25.0)
    return "Normal.\n"s;
  else if (bmi < 30.0)
    return "Overweight.\n"s;
  else
    return "Obese.\n"s;
};

auto BMI = [](double height, double mass) {
  return mass / (height * height);
};

int main() {
  double height = 1.78;
  double mass = 73.0;
  double bmi = BMI(height, mass);

  std::cout << "BMI = "s << bmi << "\n"s;
  std::cout << status(bmi);
}
