#ifndef INCLUDE_GUARD_DOUBLY_LINKEDLIST_DEQUE_HPP
#define INCLUDE_GUARD_DOUBLY_LINKEDLIST_DEQUE_HPP

#include <cassert>

#include "./doubly_linkedlist.hpp"

template <typename T>
class DoublyLinkedListDeque {
private:
  std::size_t count;
  DoublyLinkedListNode<T> *dummy;

public:
  DoublyLinkedListDeque() : count(0) {
    dummy = new DoublyLinkedListNode<T>(0);
    dummy->next = dummy;
    dummy->prev = dummy;
  }

  ~DoublyLinkedListDeque() {
    // TODO: delete all dll nodes
  }

  using Type = DoublyLinkedListNode<T>;

  // stack
  void push(T data) {
    count++;
    auto *newnode = new Type(data);

    if (this->empty()) {
      dummy->next = newnode;
      newnode->prev = dummy;

      dummy->prev = newnode;
      newnode->prev = dummy;
      return;
    }

    // latest stack elem
    dummy->prev->next = newnode;
    newnode->prev = dummy->prev;
    newnode->next = dummy;
    dummy->prev = newnode;
  }

  T pop() {
    assert(!this->empty());
    count--;
    auto delnode = dummy->prev;

    dummy->prev->prev->next = dummy;
    dummy->prev = dummy->prev->prev;

    T popped = delnode->data;
    delete delnode;
    return popped;
  }

  T top() {
    return dummy->prev->data;
  }

  // queue
  void enqueue(T data) {
    count++;
    auto *newnode = new Type(data);

    if (this->empty()) {
      dummy->next = newnode;
      newnode->prev = dummy;

      dummy->prev = newnode;
      newnode->prev = dummy;
      return;
    }

    dummy->prev->next = newnode;
    newnode->prev = dummy->prev;
    newnode->next = dummy;
    dummy->prev = newnode;
  }

  T dequeue() {
    assert(!this->empty());
    count--;
    auto delnode = dummy->next;

    dummy->next = dummy->next->next;
    dummy->next->next->prev = dummy;

    T popped = delnode->data;
    delete delnode;
    return popped;
  }

  T front() {
    return dummy->next->data;
  }

  bool empty() {
    return dummy->next == dummy && dummy->prev == dummy;
  }

  std::size_t size() const {
    return count;
  }
};

#endif /* INCLUDE_GUARD_DOUBLY_LINKEDLIST_DEQUE_HPP */