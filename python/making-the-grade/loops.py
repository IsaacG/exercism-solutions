"""Score list manipulation."""

from typing import Union


def round_scores(student_scores: list[Union[float, int]]) -> list[int]:
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    return [round(i) for i in student_scores]


def count_failed_students(student_scores: list[int]) -> int:
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    return sum(i <= 40 for i in student_scores)


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    return [i for i in student_scores if i >= threshold]


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """
    step = round((highest - 41) / 4)
    return list(range(41, highest, step))


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    return [
        f"{rank + 1}. {score}: {name}"
        for rank, (name, score) in enumerate(zip(student_scores, student_names))
    ]


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []
