CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra --pedantic-errors -Wshadow
TARGET   = a.out
SRC      = solve.cpp

run:
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

.PHONY: out
out:
	./$(TARGET)

.PHONY: in
in:
	./$(TARGET) < input
