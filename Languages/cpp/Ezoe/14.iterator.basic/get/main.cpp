#include "../../all.hpp"

auto print = [](auto x) {
  std::cout << x << "\n"s;
};

int main() {
  std::vector<int> v{1, 2, 3, 4, 5};

  auto iter = std::begin(v);
  auto end = std::end(v);

  for (; iter != end; ++iter) {
    print(*iter);
  }
}
