import zlib

content = "Hello Git"

store = "blob {}\0{}".format(len(content), content).encode("utf-8")

data = zlib.compress(store, level=1)

print(bytes.hex(data))
