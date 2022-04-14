#include "../../all.hpp"

template <typename Array>
struct array_iterator {
  Array &a;
  std::size_t i;

  array_iterator(Array &a, std::size_t i) : a(a), i(i) {}

  // prefix
  array_iterator &operator++() {
    ++i;
    return *this;
  }

  // postfix
  array_iterator operator++(int) {
    array_iterator copy = *this;
    ++*this;
    return copy;
  }

  // prefix
  array_iterator &operator--() {
    --i;
    return *this;
  }

  // postfix
  array_iterator operator--(int) {
    array_iterator copy = *this;
    --*this;
    return copy;
  }

  bool operator==(array_iterator const &right) const {
    return i == right.i;
  }

  bool operator!=(array_iterator const &right) const {
    return i != right.i;
  }

  array_iterator &operator+=(std::size_t n) {
    i += n;
    return *this;
  }

  array_iterator operator+(std::size_t n) const {
    auto copy = *this;
    copy += n;
    return copy;
  }

  typename Array::reference operator[](std::size_t n) const {
    return *(*this + n);
  }

  /* compare */
  bool operator<(array_iterator const &right) const {
    return i < right.i;
  }

  bool operator<=(array_iterator const &right) const {
    return i <= right.i;
  }

  bool operator>(array_iterator const &right) const {
    return i > right.i;
  }

  bool operator>=(array_iterator const &right) const {
    return i >= right.i;
  }

  typename Array::reference operator*() {
    return a[i];
  }
};

template <typename T, std::size_t N>
struct Array {
  // iterator
  using iterator = array_iterator<Array>;

  iterator begin() {
    return array_iterator(*this, 0);
  }

  iterator end() {
    return array_iterator(*this, N);
  }

  // members
  using value_type = T;
  using reference = T &;
  using const_reference = T const &;
  using size_type = std::size_t;

  value_type storage[N];

  reference operator[](size_type i) {
    return storage[i];
  }

  // can't change cause const
  const_reference operator[](size_type i) const {
    return storage[i];
  }

  // front()
  reference front() {
    return storage[0];
  }

  const_reference front() const {
    return storage[0];
  }

  // back()
  reference back() {
    return storage[N - 1];
  }

  const_reference back() const {
    return storage[N - 1];
  }

  void fill(T const &u) {
    for (std::size_t i = 0; i != N; ++i) {
      storage[i] = u;
    }
  }

  // size
  size_type size() const {
    return N;
  }
};
template <typename Array>
void print(Array const &c) {
  for (std::size_t i = 0; i < c.size(); ++i) {
    std::cout << c[i] << " "s;
  }
  std::cout << "\n"s;
}

auto p = [](auto x) {
  std::cout << x << "\n"s;
};

int main() {
  Array<int, 5> a = {1, 2, 3, 4, 5};
  auto iter = a.begin();

  {
    std::cout << "1 " << *iter << "\n"s;
    ++iter;
    std::cout << "2 " << *iter << "\n"s;
    --iter;
    std::cout << "3 " << *iter << "\n"s;
    iter++;
    std::cout << "4 " << *iter << "\n"s;
    iter--;
    std::cout << "5 " << *iter << "\n"s;
  }

  {
    for (auto iter = std::begin(a), last = std::end(a); iter != last; ++iter) {
      std::cout << *iter << " "s;
    }
    std::cout << "\n"s;
  }

  {
    std::for_each(std::begin(a), std::end(a),
                  [](auto x) { std::cout << x << " "s; });
    std::cout << "\n"s;
  }

  {
    p(a[3]);

    auto i = a.begin();
    p(*(i + 3));
  }

  {
    auto n = std::begin(a);
    auto m = n + 1;

    p(n < m);
    p(n <= m);
    p(n > m);
    p(n >= m);
  }
}
