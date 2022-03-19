run:
	cd build && cmake -GNinja .. && ninja

out:
	./build/a.out

.PHONY: test
test:
	cd build && cmake -GNinja .. && ninja && cd .. && ./build/test/test_out --gtest_color=yes

.PHONY: clean
clean:
	rm -r build/*
