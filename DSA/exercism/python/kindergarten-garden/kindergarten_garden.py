class Garden:
    def __init__(
        self,
        diagram: str,
        students: list = [
            "Alice",
            "Bob",
            "Charlie",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ],
    ):
        self.students = sorted(students)
        self.chunk_plants = self.split_plants(diagram)

    def split_plants(self, diagram: str) -> list:
        plants = []
        for i, row in enumerate(diagram.split()):
            for j in range(len(row) // 2):
                if i == 0:
                    plants.append(row[2 * j : 2 * j + 2])
                else:
                    plants[j] += row[2 * j : 2 * j + 2]

        return plants

    def plant(self, initial: str) -> str:
        return {
            "C": "Clover",
            "G": "Grass",
            "R": "Radishes",
            "V": "Violets",
        }.get(initial, "wow")

    def plants(self, name: str) -> list:
        idx = self.students.index(name)
        result = []

        for p in self.chunk_plants[idx]:
            result.append(self.plant(p))

        return result
