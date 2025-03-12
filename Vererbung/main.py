from enum import Enum
from typing import List, Dict
import logging
import sys

# Setup logging
logging.basicConfig(level=logging.ERROR)


# Enums for better type safety
class Gender(Enum):
    MALE = "m"
    FEMALE = "f"


# Base Person class
class Person:
    def __init__(self, name: str, gender: Gender):
        # Validate gender to ensure it is an instance of the Gender enum
        if not isinstance(gender, Gender):
            raise ValueError("Invalid gender value")
        self.name = name
        self.gender = gender


# Employee class inheriting from Person
class Employee(Person):
    def __init__(self, name: str, gender: Gender):
        # Initialize the base Person class and set department to None
        super().__init__(name, gender)
        self.department = None  # Will be set later


# DepartmentHead class inheriting from Employee
class DepartmentHead(Employee):
    def __init__(self, name: str, gender: Gender):
        # Initialize the Employee class
        super().__init__(name, gender)


# Department class
class Department:
    def __init__(self, name: str, head: DepartmentHead):
        # Validate that the head is a DepartmentHead instance
        if not isinstance(head, DepartmentHead):
            raise ValueError("Head must be a DepartmentHead instance")
        self.name = name
        self.head = head
        self.employees: List[Employee] = []  # Initialize an empty list of employees

    def add_employee(self, employee: Employee):
        # Validate that the added employee is an instance of Employee
        if not isinstance(employee, Employee):
            raise ValueError("Invalid employee")
        # Assign the employee to this department and add them to the list
        employee.department = self
        self.employees.append(employee)

    def employee_count(self) -> int:
        # Return the number of employees in the department
        return len(self.employees)


# Company class
class Company:
    def __init__(self, name: str):
        self.name = name
        self.departments: List[Department] = []  # Initialize an empty list of departments

    def add_department(self, department: Department):
        # Validate that the added department is an instance of Department
        if not isinstance(department, Department):
            raise ValueError("Invalid department")
        self.departments.append(department)

    def total_employee_count(self) -> int:
        # Calculate the total number of employees across all departments
        return sum(dept.employee_count() for dept in self.departments)

    def total_department_heads(self) -> int:
        # Return the number of department heads (equal to the number of departments)
        return len(self.departments)

    def total_departments(self) -> int:
        # Return the total number of departments in the company
        return len(self.departments)

    def largest_department(self) -> Department:
        # Find the department with the most employees, or return None if no departments exist
        return max(self.departments, key=lambda dept: dept.employee_count(), default=None)

    def gender_percentage(self) -> Dict[str, float]:
        # Calculate the gender distribution as percentages
        total = 0
        gender_count = {Gender.MALE: 0, Gender.FEMALE: 0}
        for department in self.departments:
            for employee in department.employees:
                gender_count[employee.gender] += 1
                total += 1

        # Handle the case where there are no employees
        if total == 0:
            return {gender.name.lower(): 0.0 for gender in Gender}

        # Return percentages for each gender
        return {
            gender.name.lower(): (count / total) * 100
            for gender, count in gender_count.items()
        }


def my_cli():
    try:
        # Example instantiation of objects
        head1 = DepartmentHead("Anna", Gender.FEMALE)
        department1 = Department("IT", head1)

        head2 = DepartmentHead("Tom", Gender.MALE)
        department2 = Department("HR", head2)

        employee1 = Employee("John", Gender.MALE)
        employee2 = Employee("Lisa", Gender.FEMALE)
        employee3 = Employee("Max", Gender.MALE)

        # Adding employees to departments
        department1.add_employee(employee1)
        department1.add_employee(employee2)
        department2.add_employee(employee3)

        # Creating a company and adding departments
        company = Company("TechCorp")
        company.add_department(department1)
        company.add_department(department2)

        # Outputs of company methods
        print(f"Total number of employees: {company.total_employee_count()}")
        print(f"Total number of department heads: {company.total_department_heads()}")
        print(f"Total number of departments: {company.total_departments()}")

        # Find and print the largest department
        largest_dept = company.largest_department()
        if largest_dept:
            print(f"Largest department: {largest_dept.name} with {largest_dept.employee_count()} employees")

        # Print the gender distribution in the company
        print(f"Gender distribution: {company.gender_percentage()}")

    except Exception as error:
        # Log any unexpected errors and exit with a status code of 1
        logging.error(f"An error occurred: {error}")
        sys.exit(1)


if __name__ == '__main__':
    my_cli()
