#include "../../all.hpp"

auto print_all = [](auto first, auto last) {
  for (auto iter = first; iter != last; ++iter) {
    std::cout << *iter;
  }
};

// f can take function()
auto call_func = [](auto f) {
  f(123);
  std::cout << "\n"s;
};

auto print = [](auto x) {
  std::cout << x;
};

auto print_new_line = [](auto x) {
  std::cout << x << "\n"s;
};

auto twice = [](auto x) {
  std::cout << 2 * x;
};

auto for_each = [](auto first, auto last, auto f) {
  std::cout << ">>> for_each\n"s;

  for (auto iter = first; iter != last; ++iter) {
    f(*iter);
  }

  std::cout << "\n\n"s;
};

int main() {
  std::vector<int> v{1, 2, 3, 4, 5};

  for (auto i = std::begin(v), j = std::end(v); i != j; ++i) {
    std::cout << *i << "\n"s;
  }

  print_all(std::begin(v), std::end(v));

  call_func(print);
  call_func(twice);

  for_each(std::begin(v), std::end(v), print);
  for_each(std::begin(v), std::end(v), twice);
  for_each(std::begin(v), std::end(v), print_new_line);
  for_each(std::begin(v), std::end(v),
           [](auto v) { std::cout << "- " << v << "\n"s; });
  std::for_each(std::begin(v), std::end(v),
                [](auto v) { std::cout << v << "\n"s; });
}
