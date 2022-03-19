#include <gtest/gtest.h>

#include <iostream>

#include "../include/singly_linkedlist.hpp"

TEST(TestSinglyLinkedListNode, test) {
  SinglyLinkedListNode<int> *head = new SinglyLinkedListNode<int>();
  head->next = new SinglyLinkedListNode<int>(1);
  head->next->next = new SinglyLinkedListNode<int>(2);
  head->next->next->next = new SinglyLinkedListNode<int>(3);
  head->next->next->next->next = new SinglyLinkedListNode<int>(4);

  EXPECT_EQ(head->data, 0);
  head = head->next;
  EXPECT_EQ(head->data, 1);
  head = head->next;
  EXPECT_EQ(head->data, 2);
  head = head->next;
  EXPECT_EQ(head->data, 3);
  head = head->next;
  EXPECT_EQ(head->data, 4);
}

TEST(TestSinglyLinkedListNode, copy) {
  SinglyLinkedListNode<char> *head = new SinglyLinkedListNode<char>('a');
  auto copy = head;
  EXPECT_EQ(head->data, 'a');
  EXPECT_EQ(copy->data, 'a');
}
