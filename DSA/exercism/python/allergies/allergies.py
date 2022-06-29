class Allergies:
    eggs = 0b_0000_0001
    peanuts = 0b_0000_0010
    shellfish = 0b_0000_0100
    strawberries = 0b_0000_1000
    tomatoes = 0b_0001_0000
    chocolate = 0b_0010_0000
    pollen = 0b_0100_0000
    cats = 0b_1000_0000

    def __init__(self, score: int):
        self.score = score

    def allergic_to(self, item: str) -> bool:
        if item == "eggs":
            return self.score & Allergies.eggs != 0
        if item == "peanuts":
            return self.score & Allergies.peanuts != 0
        if item == "shellfish":
            return self.score & Allergies.shellfish != 0
        if item == "strawberries":
            return self.score & Allergies.strawberries != 0
        if item == "tomatoes":
            return self.score & Allergies.tomatoes != 0
        if item == "chocolate":
            return self.score & Allergies.chocolate != 0
        if item == "pollen":
            return self.score & Allergies.pollen != 0
        if item == "cats":
            return self.score & Allergies.cats != 0

        return False

    @property
    def lst(self) -> list:
        allergics = [
            "eggs",
            "peanuts",
            "shellfish",
            "strawberries",
            "tomatoes",
            "chocolate",
            "pollen",
            "cats",
        ]

        res = []

        for allergic in allergics:
            if self.allergic_to(allergic):
                res.append(allergic)

        return res
