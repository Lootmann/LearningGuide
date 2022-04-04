#include "../../all.hpp"

void desc(std::vector<int> &v) {
  std::size_t size = v.size();

  for (std::size_t head = 0; head != size; ++head) {
    std::size_t min = head;

    for (std::size_t i = head + 1; i != size; ++i) {
      if (v.at(i) < v.at(min)) {
        min = i;
      }
    }

    auto temp = v.at(head);
    v.at(head) = v.at(min);
    v.at(min) = temp;
  }
}

int main() {
  std::vector<int> v{8, 3, 7, 4, 2, 9, 3};

  desc(v);

  // index
  for (auto num : v) {
    std::cout << num << " "s;
  }

  std::cout << "\n"s;
}
