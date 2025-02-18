import dataclasses
from typing import List
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int or float


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_students = max(len(group.students)
                       for group in groups) if groups else 0
    return max_students


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialties = set()
    for group in groups:
        specialties.add(group.specialty.name)

    return list(specialties)


def read_students_information() -> Student:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
