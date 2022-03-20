#ifndef INCLUDE_GUARD_DOUBLY_LINKEDLIST_HPP
#define INCLUDE_GUARD_DOUBLY_LINKEDLIST_HPP

// doubly linked list node
template <class T>
class DoublyLinkedListNode {
public:
  T data;
  DoublyLinkedListNode<T> *next, *prev;

  DoublyLinkedListNode(T data = T()) : data(data) {}
};

#endif /* INCLUDE_GUARD_DOUBLY_LINKEDLIST_HPP */