#include <gtest/gtest.h>

#include <vector>

#include "../include/array_stack.hpp"
#include "test_macro.hpp"

TEST(ArrayStack, empty_stack) {
  ArrayStack<char> arr;

  EXPECT_EQ(arr.size(), 0);
  EXPECT_TRUE(arr.empty());
}

TEST(ArrayStack, push) {
  ArrayStack<int> arr;

  REP(i, 5) arr.push(i);
  EXPECT_EQ(arr.size(), 5);
  EXPECT_FALSE(arr.empty());
}

TEST(ArrayStack, pop) {
  ArrayStack<char> arr;

  arr.push('a');
  arr.push('b');
  arr.push('c');

  EXPECT_EQ(arr.pop(), 'c');
  EXPECT_EQ(arr.pop(), 'b');
  EXPECT_EQ(arr.pop(), 'a');
}

TEST(ArrayStack, top) {
  ArrayStack<char> arr;

  std::vector<char> tests{};
  REP(i, 26) tests.emplace_back((char)((int)'a' + i));

  for (auto const ch : tests) {
    arr.push(ch);
    EXPECT_EQ(arr.top(), ch);
  }
}

TEST(ArrayStack, Huge) {
  ArrayStack<int> arr;

  REP(i, 1000000) {
    arr.push(i);
    EXPECT_EQ(arr.pop(), i);
  }
}
