from abc import ABC, abstractmethod
from random import randint, choice
from faker import Faker

fake = Faker(locale='uk_UA')


class SchoolPersonnel(ABC):
    """
    Abstract Class School Personnel
    """

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def __str__(self):
        pass


class Teacher(SchoolPersonnel):
    """
    Class Teacher
    """

    def __str__(self):
        return 'Hello my name', self.name, 'I"m a Teacher with salary', self.salary

    def __repr__(self):
        return f'Teacher {self.name}'


class Technician(SchoolPersonnel):
    """
    Class of technical personnel
    """

    def __str__(self):
        return 'Hello my name', self.name, 'I"m a Technical with salary', self.salary

    def __repr__(self):
        return f'Technician {self.name}'


class School:
    """
    This is class School
    """

    def __init__(self, school_name: str, school_principal: Teacher, number_of_teachers: int = 11,
                 number_of_technicians: int = 4):
        self.school_name = school_name
        self.principal = school_principal
        self.teachers = [Teacher(fake.name(), randint(6500, 50000)) for position in range(number_of_teachers)]
        self.technicians = [Technician(fake.name(), randint(3000, 8000)) for position in range(number_of_technicians)]

    @property
    def school_total_salary(self):
        """
        This function returns total school salary
        :return: total
        """
        all_personnel = [self.principal]
        all_personnel += self.teachers
        all_personnel += self.technicians
        total = sum((obj.salary for obj in all_personnel))
        return total

    def appoint_new_principal(self):
        """
        This function appoints new principal and removes him from list of teachers
        Old principal is added to list of teachers
        """
        old_principal = self.principal
        candidate = self.teachers.pop(4)
        self.principal = candidate
        self.teachers.append(old_principal)


gymnasium_21 = School('Gymnasium 21', Teacher('Dimochka', 10000))
list_of_teachers = gymnasium_21.teachers
school_salary = gymnasium_21.school_total_salary
gymnasium_21.teachers.append(Teacher('Volodka', 90000))
list_of_teachers2 = gymnasium_21.teachers
school_salary2 = gymnasium_21.school_total_salary
gymnasium_21.appoint_new_principal()
