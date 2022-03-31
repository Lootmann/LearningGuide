#include "../../all.hpp"

int main() {
  auto print = [](std::size_t size) {
    std::cout << size << "\n"s;
  };

  print(sizeof(float));
  print(sizeof(double));
  print(sizeof(long double));

  {
    float a = 10000;
    float b = 0.0001;
    float c = a + b;
    print(c);
  }

  {
    auto a = 123.456f;
    auto b = 123.456F;
    auto c = 123.456;

    auto d = 123.456l;
    auto e = 123.456L;
  }

  {
    std::cout << ">>> significant digits\n"s;

    print(std::numeric_limits<float>::digits10);
    print(std::numeric_limits<float>::epsilon());

    print(std::numeric_limits<double>::digits10);
    print(std::numeric_limits<double>::epsilon());

    print(std::numeric_limits<long double>::digits10);
    print(std::numeric_limits<long double>::epsilon());
  }

  {
    print(1.0f + 1.0f);
    print(1.0f + 1.0);
    print(1.0f + 1.01);
  }
}
