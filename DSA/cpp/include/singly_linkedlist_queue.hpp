#ifndef INCLUDE_GUARD_SINGLY_LINKEDLIST_QUEUE
#define INCLUDE_GUARD_SINGLY_LINKEDLIST_QUEUE

#include <iostream>

#include "./singly_linkedlist.hpp"

template <typename T>
class SinglyLinkedListQueue {
private:
  std::size_t count;
  SinglyLinkedListNode<T> *head, *tail;

public:
  SinglyLinkedListQueue() : count(0), head(nullptr), tail(nullptr) {}
  ~SinglyLinkedListQueue() {}

  using Type = SinglyLinkedListNode<T>;

  void enqueue(T data) {
    count++;
    if (this->empty()) {
      head = tail = new Type(data);
      return;
    }

    auto *new_node = new Type(data);
    tail->next = new_node;
    tail = new_node;
  }

  T dequeue() {
    assert(!this->empty());
    count--;

    T que = head->data;

    // this is a last element when queue.size == 1
    if (head == tail) {
      head = tail = nullptr;
      return que;
    }

    head = head->next;
    return que;
  }

  T front() {
    assert(!this->empty());
    return head->data;
  }

  bool empty() {
    return head == nullptr && tail == nullptr;
  }

  std::size_t size() const {
    return count;
  }
};

#endif /* INCLUDE_GUARD_SINGLY_LINKEDLIST_QUEUE */
