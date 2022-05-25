"""Functions for organizing and calculating student exam scores."""
from typing import List, Union

Type = Union[int, float]


def round_scores(student_scores: List[Type]) -> List[int]:
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    return list(map(round, student_scores))


def count_failed_students(student_scores: List[int]):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    return sum(map(lambda x: x <= 40, student_scores))


def above_threshold(student_scores: List[int], threshold: int) -> List[int]:
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    return list(filter(lambda x: x >= threshold, student_scores))


def letter_grades(highest: int) -> List[int]:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    interval = (highest - 40) // 4
    return [40 + idx * interval + 1 for idx in range(4)]


def student_ranking(student_scores: List[int], student_names: List[str]) -> List[str]:
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    result = []
    for idx, (score, name) in enumerate(zip(student_scores, student_names)):
        result.append(f"{idx+1}. {name}: {score}")
    return result


def perfect_score(student_infos: List[list]) -> List[int]:
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for info in student_infos:
        if info[1] == 100:
            return info
    return []
