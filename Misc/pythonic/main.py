def title(msg: str) -> None:
    print("\n>>> {}".format(msg))


def main():
    title("enumerate")
    books = ["django for beginner", "django for professionals", "Expert Python"]

    for i, bookname in enumerate(books):
        print(i, bookname)

    title("raw string")
    print(r"/home/foo/bar/usr/locate")

    title("f-string")
    name = "lyo"
    print("hello %s :^)" % name)
    print("hello {} :^)".format(name))
    print(f"hello {name} :^)")

    title("list copy")
    lst1 = [1, 2, 3]
    lst2 = lst1
    print(lst1, lst2)

    lst2[1] = 10
    print(lst1, lst2)

    title("dict.get()")
    fruits = {"apple": 2}
    print(fruits.get("apple", 1))
    print(fruits.get("banana", 0))


if __name__ == "__main__":
    main()
