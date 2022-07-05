from collections import defaultdict
from typing import List


class School:
    def __init__(self):
        self._grade = defaultdict(list)
        self._added = []

    def add_student(self, name: str, grade: int) -> None:
        """add_student
        add student dict {grade:name}
        if 'name' is duplicated, it will not be added to self._grade[name] list.

        :param name: str
        :return: None
        """
        for added_names in self._grade.values():
            if name in added_names:
                self._added.append(False)
                return

        self._added.append(True)
        self._grade[grade].append(name)

    def roster(self) -> List[str]:
        res = []
        for grade in sorted(self._grade.keys()):
            name_by_grades = []
            for name in self._grade[grade]:
                name_by_grades.append(name)
            res += sorted(name_by_grades)

        return res

    def grade(self, grade_number) -> List[str]:
        res = []
        for grade, name in self._grade.items():
            if grade == grade_number:
                res += name
        return sorted(res)

    def added(self) -> list:
        return self._added
