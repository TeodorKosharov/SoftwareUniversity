class Class:
    __students_count = 22  # Когато имаме такава променлива с две долни черти, я извикваме не със self, а с името на класа - Class.__students_count

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        avg = sum(self.grades) / len(self.grades)
        return round(avg, 2)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"
