#include "../../all.hpp"

struct fractional {
  int num;
  int denom;

  fractional(int num) : num(num), denom(1) {}
  fractional(int num, int denom) : num(num), denom(denom) {}
};

fractional operator+(fractional& l, fractional& r) {
  if (l.denom == r.denom) return fractional{l.num + r.num, l.denom};
  return fractional{l.num * r.denom + r.num * l.denom, l.denom * r.denom};
}

fractional operator-(fractional& l, fractional& r) {
  if (l.denom == r.denom) return fractional{l.num - r.num, l.denom};
  return fractional{l.num * r.denom - r.num * l.denom, l.denom * r.denom};
}

fractional operator*(fractional& l, fractional& r) {
  return fractional{l.num * r.num, l.denom * r.denom};
}

fractional operator/(fractional& l, fractional& r) {
  return fractional{l.num * r.denom, l.denom * r.num};
}

int main() {
  fractional a{2, 3};
  fractional b{4, 3};

  auto c = a + b;
  auto d = a - b;
  auto e = a * b;
  auto f = a / b;
}
