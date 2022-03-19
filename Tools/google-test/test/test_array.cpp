#include <gtest/gtest.h>

#include <iostream>

#include "../include/Array.hpp"

TEST(TestArray, test) {
  Array<int> arr(5);

  for (std::size_t i = 0; i < 5; ++i) {
    arr[i] = i;
  }

  for (std::size_t i = 0; i < 5; ++i) {
    EXPECT_EQ(arr[i], i);
  }
}

TEST(TestArray, length) {
  Array<int> arr(5);
  EXPECT_EQ(arr.size(), 5);
}
