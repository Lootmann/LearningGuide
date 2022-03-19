#include <gtest/gtest.h>

#include <vector>

#include "../include/singly_linkedlist_stack.hpp"
#include "./test_macro.hpp"

class SinglyLinkedListStackTest : public ::testing::Test {
protected:
  virtual void setUp() {}
  SinglyLinkedListStack<int> sll;
};

TEST_F(SinglyLinkedListStackTest, init) {
  EXPECT_EQ(sll.size(), 0);
  EXPECT_TRUE(sll.empty());
}

TEST_F(SinglyLinkedListStackTest, push) {
  REP(i, 100) {
    sll.push(i);
    EXPECT_EQ(sll.top(), i);
    EXPECT_EQ(sll.size(), i + 1);
  }
}

TEST_F(SinglyLinkedListStackTest, pop) {
  REP(i, 100 + 1) sll.push(i);
  REPR(i, 100) EXPECT_EQ(sll.pop(), i);

  EXPECT_TRUE(sll.empty());
  EXPECT_EQ(sll.size(), 0);
}

TEST_F(SinglyLinkedListStackTest, empty) {
  EXPECT_TRUE(sll.empty());
  sll.push(1);
  EXPECT_FALSE(sll.empty());
  sll.pop();
  EXPECT_TRUE(sll.empty());
}
