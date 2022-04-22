#include "../../all.hpp"

struct C {
  int data;

  void m_func() {
    std::cout << "data = " << data << "\n"s;
  }

  void set(int n) {
    C* pointer = this;
    pointer->data = n;
  }

  void f() {
    // reference this to ref
    auto& this_ref = *this;
    std::cout << this_ref.data << "\n"s;
  }

  void f() const {
    C const* pointer = this;
    std::cout << pointer->data << "\n"s;
  }
};

int main() {
  C object;
  object.data = 10;
  object.m_func();

  C* pointer = &object;
  (*(pointer)).data = 20;
  (*(pointer)).m_func();
  pointer->m_func();

  pointer->set(30);
  pointer->m_func();

  pointer->f();
}
