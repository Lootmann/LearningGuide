"""
Function name should be a good name that allows you
to image what the process will be.
"""

from typing import Any


def title(msg: str):
    print()
    print(f">>> {msg}")


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"name: {self.name}, age: {self.age}"


class Animal:
    def __init__(self):
        pass


def person_as_dict(person: Person) -> dict:
    return {
        "name": person.name,
        "age": person.age,
    }


def is_person(obj: Any) -> bool:
    """is_person
    check Person instance

    Args:
        obj: Any
    Returns:
        bool - return True if obj is Person instance
    """
    return isinstance(obj, Person)


class Model:
    def __init__(self):
        print("Model init")

    def save(self):
        print("saved :^)")


class ArticleModel(Model):
    def __init__(self, title: str):
        super().__init__()
        self.title = title


def is_valid_title(title: str) -> bool:
    if len(title) > 10:
        return False

    return True


def main():
    title("person")
    person = Person(name="James", age=35)
    person_dict = person_as_dict(person)

    print(person)
    print(person_dict)

    animal = Animal()
    print(is_person(person))
    print(is_person(animal))

    title("Article Model")
    article = ArticleModel(title="new article")
    article.save()


if __name__ == "__main__":
    main()
