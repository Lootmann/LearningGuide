#include <gtest/gtest.h>

#include <iostream>
#include <vector>

#include "../include/doubly_linkedlist_deque.hpp"
#include "./test_macro.hpp"

class DoublyLinkedListDequeTest : public ::testing::Test {
protected:
  virtual void setUp() {}
  DoublyLinkedListDeque<int> sll;
  std::vector<int> vi{};
};

TEST_F(DoublyLinkedListDequeTest, init) {
  EXPECT_EQ(sll.size(), 0);
  EXPECT_TRUE(sll.empty());
}

TEST_F(DoublyLinkedListDequeTest, stack) {
  REP(i, 100) vi.emplace_back(i);

  // push
  for (auto test : vi) {
    sll.push(test);
    EXPECT_EQ(sll.top(), test);
  }

  // pop
  EXPECT_EQ(sll.size(), vi.size());

  for (int i = (int)vi.size() - 1; i >= 0; --i) {
    EXPECT_EQ(sll.pop(), vi[i]);
    EXPECT_EQ(sll.size(), i);
  }
}