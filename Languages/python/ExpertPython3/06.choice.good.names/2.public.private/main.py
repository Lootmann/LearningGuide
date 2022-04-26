class Citizen:
    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self) -> str:
        return f"{self._first_name} {self._last_name}"


class DB:
    is_connected = False
    has_cache = False

    connected_users = ["Tarek"]
    tables = {"Customer": ["id", "first_name", "last_name"]}


def main():
    c = Citizen(first_name="Brown", last_name="James")
    print(c.full_name)


if __name__ == "__main__":
    main()
