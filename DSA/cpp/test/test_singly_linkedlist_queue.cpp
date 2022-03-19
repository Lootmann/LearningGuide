#include <gtest/gtest.h>

#include "../include/singly_linkedlist_queue.hpp"
#include "./test_macro.hpp"

class SinglyLinkedListQueueTest : public ::testing::Test {
protected:
  virtual void setUp() {}
  SinglyLinkedListQueue<int> sll;
};

TEST_F(SinglyLinkedListQueueTest, init) {
  EXPECT_EQ(sll.size(), 0);
  EXPECT_TRUE(sll.empty());
}

TEST_F(SinglyLinkedListQueueTest, enqueue) {
  int first = 1;
  sll.enqueue(first);

  REP(i, 10000) {
    sll.enqueue(i);
    EXPECT_EQ(sll.front(), first);
  }
}

TEST_F(SinglyLinkedListQueueTest, dequeue) {
  REP(i, 100000) sll.enqueue(i);
  REP(i, 100000) EXPECT_EQ(sll.dequeue(), i);

  EXPECT_EQ(sll.size(), 0);
  EXPECT_TRUE(sll.empty());
}

TEST_F(SinglyLinkedListQueueTest, size) {
  REP(i, 100000) sll.enqueue(i);
  EXPECT_EQ(sll.size(), 100000);
}
