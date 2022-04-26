class InitOnAccess:
    def __init__(self, klass, *args, **kwgs):
        self.klass = klass
        self.args = args
        self.kwgs = kwgs
        self._initialized = None

    def __get__(self, instance, owner):
        if self._initialized is None:
            print("Inited")
            self._initialized = self.klass(*self.args, **self.kwgs)
        else:
            print("still inited")
        return self._initialized


class MyClass:
    lazily_initialized = InitOnAccess(list, "argument")


class lazy_property:
    def __init__(self, function) -> None:
        self.fget = function

    def __get__(self, obj, cls):
        value = self.fget(obj)
        setattr(obj, self.fget.__name__, value)
        return value


def main():
    m = MyClass()
    m.lazily_initialized
    m.lazily_initialized


if __name__ == "__main__":
    main()
