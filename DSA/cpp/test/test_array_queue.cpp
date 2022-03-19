#include <gtest/gtest.h>

#include <iostream>
#include <vector>

#include "../include/array_queue.hpp"
#include "test_macro.hpp"

class QueueTest : public ::testing::Test {
protected:
  virtual void setUp() {}
  ArrayQueue<int> que;
};

TEST_F(QueueTest, size) {
  REP(i, 10) {
    que.enqueue(i);
    EXPECT_EQ(que.size(), i + 1);
  }
}

TEST_F(QueueTest, enqueue) {
  REP(i, 10) {
    que.enqueue(1);
  }
  EXPECT_EQ(que.size(), 10);
}

TEST_F(QueueTest, dequeue) {
  REP(i, 10) {
    que.enqueue(i);
    EXPECT_EQ(que.dequeue(), i);
  }
}

TEST_F(QueueTest, front) {
  que.enqueue(1);
  REP(i, 10) {
    que.enqueue(i);
    EXPECT_EQ(que.front(), 1);
  }
}

TEST_F(QueueTest, Huge) {
  REP(i, 1000000) {
    que.enqueue(i);
    EXPECT_EQ(que.dequeue(), i);
  }
  EXPECT_EQ(que.size(), 0);
}