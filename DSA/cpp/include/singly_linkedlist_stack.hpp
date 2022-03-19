#ifndef INCLUDE_GUARD_SINGLY_LINKEDLIST_STACK
#define INCLUDE_GUARD_SINGLY_LINKEDLIST_STACK

#include <cassert>
#include <iostream>

#include "./singly_linkedlist.hpp"

template <typename T>
class SinglyLinkedListStack {
private:
  std::size_t count;
  SinglyLinkedListNode<T> *head;

public:
  SinglyLinkedListStack() : count(0), head(nullptr) {}
  ~SinglyLinkedListStack() {}

  using Type = SinglyLinkedListNode<T>;

  void push(T data) {
    count++;
    if (this->empty()) {
      head = new Type(data);
      return;
    }

    auto *new_node = new Type(data);
    new_node->next = head;
    head = new_node;
  }

  T pop() {
    assert(empty() == false);
    count--;
    T popped = head->data;
    head = head->next;
    return popped;
  }

  T top() {
    return head->data;
  }

  bool empty() {
    return head == nullptr;
  }

  std::size_t size() const {
    return count;
  }
};

#endif /* INCLUDE_GUARD_SINGLY_LINKEDLIST_STACK */
