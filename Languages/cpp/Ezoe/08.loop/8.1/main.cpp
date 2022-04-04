#include "../../all.hpp"

auto title = [](auto msg) {
  std::cout << "\n--- "s << msg << "\n"s;
};

void loop_while() {
  int i = 0;
  while (i < 10) {
    std::cout << i << " "s;
    i += 1;
  }
  std::cout << "\n"s;

  int k = 0;
  while (true) {
    if (k > 9) break;
    std::cout << k << " "s;
    k += 1;
  }
  std::cout << "\n"s;
}

void loop_for() {
  for (int i = 0; i <= 100; ++i) {
    std::cout << i << " "s;
  }
  std::cout << "\n"s;
}

void loop_do() {
  do {
    std::cout << "do once at least"s;
  } while (false);

  std::cout << "\n"s;
}

int main() {
  title("while");
  loop_while();

  title("for");
  loop_for();

  title("do-while");
  loop_do();
}
