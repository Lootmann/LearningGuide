cmake_minimum_required(VERSION 3.12)

add_library(Lib
  STATIC
  ./array.cpp
  ./array_minstack.cpp
  ./array_queue.cpp
  ./array_stack.cpp
  ./singly_linkedlist.cpp
  ./singly_linkedlist_queue.cpp
  ./singly_linkedlist_stack.cpp
  ./doubly_linkedlist.cpp
  )

target_include_directories(Lib
  PUBLIC ${PROJECT_SOURCE_DIR}/include
  )
