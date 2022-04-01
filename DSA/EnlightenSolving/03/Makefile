CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra --pedantic-errors -Wshadow
TARGET   = a.out
SRC      = 3.2.cpp

run:
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

.PHONY: out
out:
	./$(TARGET)

.PHONY: in
in:
	./$(TARGET) < in
