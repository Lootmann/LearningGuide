gcc_options = -std=c++2a -Wall -pedantic-errors

program: main.cpp
	g++ $(gcc_options) $< -o $@

run: program
	./program

clean:
	rm -f ./program

.PHONY: run clean
