class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix = matrix_string.split("\n")

    def row(self, index: int) -> list:
        result = []

        print(self.matrix)

        for num in self.matrix[index - 1].split(" "):
            result.append(int(num))

        return result

    def column(self, index: int) -> list:
        result = []

        print(self.matrix)
        for row in self.matrix:
            print(row)
            result.append(int(row.split(" ")[index - 1]))

        return result
