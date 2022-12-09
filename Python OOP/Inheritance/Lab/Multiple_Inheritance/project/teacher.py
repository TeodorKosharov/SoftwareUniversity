from Lab.Multiple_Inheritance.project.person import Person
from Lab.Multiple_Inheritance.project.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'
