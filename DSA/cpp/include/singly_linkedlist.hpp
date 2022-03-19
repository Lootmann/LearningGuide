#ifndef INCLUDE_GUARD_NODE_HPP
#define INCLUDE_GUARD_NODE_HPP

#include <iostream>

// singly linked list node
template <class T>
class SinglyLinkedListNode {
public:
  T data;
  SinglyLinkedListNode<T> *next;
  SinglyLinkedListNode(T data = T()) : data(data) {}

  // destructor
  ~SinglyLinkedListNode<T>() {
    delete next;
  }

  // copy constructor
  // SinglyLinkedListNode(const SinglyLinkedListNode<T> &) = delete;
  // move constructor
  // SinglyLinkedListNode(SinglyLinkedListNode<T> &&) = delete;
  // copy assign operator
  // SinglyLinkedListNode &operator=(const SinglyLinkedListNode<T> &) = delete;
  // move operator
  // SinglyLinkedListNode &operator=(const SinglyLinkedListNode<T> &&) = delete;
};

#endif /* INCLUDE_GUARD_NODE_HPP */
