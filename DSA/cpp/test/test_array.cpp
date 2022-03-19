#include <gtest/gtest.h>

#include <iostream>
#include <vector>

#include "../include/array.hpp"

TEST(TestArray, operator_equal) {
  Array<int> arr(5);

  for (std::size_t i = 0; i < arr.size(); ++i) {
    arr[i] = i;
  }

  EXPECT_EQ(arr[0], 0);
  EXPECT_EQ(arr[1], 1);
  EXPECT_EQ(arr[2], 2);
  EXPECT_EQ(arr[3], 3);
  EXPECT_EQ(arr[4], 4);
}

TEST(TestArray, move) {
  Array<int> arr1(3);

  for (std::size_t i = 0; i < arr1.size(); ++i) {
    arr1[i] = i;
  }

  Array<int> arr2(3);
  // move, arr1 is no longer usable.
  arr2 = arr1;

  for (std::size_t i = 0; i < arr2.size(); ++i) {
    arr2[i] = i;
  }
}

TEST(TestArray, resize) {
  Array<int> arr(0);
  EXPECT_EQ(arr.size(), 0);
  std::vector<int> sizes{1, 2, 4, 8, 16, 32, 64, 128};

  for (auto const size : sizes) {
    arr.resize();
    EXPECT_EQ(arr.size(), size);
  }
}
