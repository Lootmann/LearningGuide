#include <gtest/gtest.h>

#include <algorithm>
#include <iostream>
#include <random>
#include <vector>

#include "../include/array_minstack.hpp"
#include "test_macro.hpp"

class MinStackTest : public ::testing::Test {
protected:
  virtual void setUp() {}
  ArrayMinStack<int> arr;
};

TEST_F(MinStackTest, init) {
  EXPECT_EQ(arr.size(), 0);
  EXPECT_TRUE(arr.empty());
}

TEST_F(MinStackTest, push_for) {
  for (int i = 1; i <= 10; ++i) arr.push(i);
  EXPECT_EQ(arr.size(), 10);
  EXPECT_EQ(arr.top(), 10);
}

TEST_F(MinStackTest, push_reverse) {
  for (int i = 10; i > 0; --i) arr.push(i);
  EXPECT_EQ(arr.size(), 10);
  EXPECT_EQ(arr.top(), 1);
}

TEST_F(MinStackTest, pop) {
  std::vector<int> tests{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  for (auto t : tests) arr.push(t);

  for (auto it = tests.rbegin(); it != tests.rend(); ++it) {
    auto stack = arr.pop();
    EXPECT_EQ(stack.data, *it);
    EXPECT_EQ(stack.min, 0);
    EXPECT_EQ(arr.size(), *it);
  }
}

TEST_F(MinStackTest, pop_min) {
  std::vector<int> tests{20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10};
  for (auto t : tests) arr.push(t);

  for (auto it = tests.rbegin(); it != tests.rend(); ++it) {
    auto stack = arr.pop();
    EXPECT_EQ(stack.data, *it);
    EXPECT_EQ(stack.min, *it);
    EXPECT_EQ(arr.size(), 20 - *it);
  }
}

TEST_F(MinStackTest, random_test) {
  std::mt19937 engine(std::random_device{}());
  std::uniform_int_distribution<int> dist(1, 100000);

  int stack_value{};
  int min_value{100000};
  REP(i, 10) {
    int random_value = dist(engine);
    arr.push(random_value);
    min_value = std::min(min_value, random_value);
    stack_value = random_value;
  }

  EXPECT_EQ(arr.min(), min_value);
  EXPECT_EQ(arr.top(), stack_value);
}
