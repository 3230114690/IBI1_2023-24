class Student:
    def __init__(self, name, major, portfolio_score, project_score, exam_score):
        self.name = name
        self.major = major
        self.portfolio_score = portfolio_score
        self.project_score = project_score
        self.exam_score = exam_score

    def print_details(self):
        print(f"Name: {self.name}, Major: {self.major}, Portfolio Score: {self.portfolio_score}, "
              f"Project Score: {self.project_score}, Exam Score: {self.exam_score}")

# Example usage:
student1 = Student("John Doe", "BMI", 85, 90, 78)
student1.print_details()
