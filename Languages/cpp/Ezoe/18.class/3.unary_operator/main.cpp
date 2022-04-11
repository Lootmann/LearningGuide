#include "../../all.hpp"

struct IntLike {
  int data;

  IntLike(int data = 0) : data(data) {}

  IntLike operator+(IntLike const& right) {
    return IntLike{data + right.data};
  }
};

IntLike operator+(IntLike const& obj) {
  return obj;
}

IntLike& operator++(IntLike& obj) {
  ++obj.data;
  return obj;
}

IntLike operator++(IntLike& obj, int) {
  auto temp = obj;
  ++obj.data;
  return temp;
}

IntLike operator-(IntLike const& obj) {
  return IntLike{-obj.data};
}

IntLike& operator--(IntLike& obj) {
  --obj.data;
  return obj;
}

IntLike operator--(IntLike& obj, int) {
  auto temp = obj;
  --obj.data;
  return temp;
}

int main() {
  IntLike a{1}, b{2};
  auto c = a + b;

  std::cout << c.data << "\n"s;

  c--;
  std::cout << c.data << "\n"s;

  c++;
  std::cout << c.data << "\n"s;

  c--;
  std::cout << c.data << "\n"s;
}
