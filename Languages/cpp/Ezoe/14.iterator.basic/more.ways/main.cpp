#include "../../all.hpp"

auto output_all = [](auto first, auto last) {
  std::cout << ">>> output_all\n"s;
  for (auto iter = first; iter != last; ++iter) {
    std::cout << *iter << "\n"s;
  }
  std::cout << "\n"s;
};

int main() {
  {
    std::vector<int> v{1, 2, 3, 4, 5};
    output_all(std::begin(v), std::end(v));
  }

  {
    std::filesystem::directory_iterator first("./"), last;
    output_all(first, last);
  }
}
