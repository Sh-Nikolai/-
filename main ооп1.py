class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.aver_sum}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}'
        return res

    def aver_sum(self):
        sum = 0
        count = 0

        for value in self.grades.values():
            sum += value
            count += 1
        print(sum / count, 2)



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.aver_sum}'
        return res

    def aver_sum(self):
        sum = 0
        count = 0

        for value in self.grades.values():
            sum += value
            count += 1
        print(sum / count, 2)



class Reviewer (Mentor):

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res




    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_lecture = Lecturer('Ruoy', 'Eman', 'your_gender')
best_lecture.courses_in_progress += ['Python']

cool_student = Student ('Some', 'Buddy', 'your_gender')
cool_student.courses_attached += ['Python']

cool_student.rate_hw(best_lecture, 'Python', 10)
cool_student.rate_hw(best_lecture, 'Python', 10)
cool_student.rate_hw(best_lecture, 'Python', 10)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer ('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)



print(best_student.grades)
print(best_lecture.grades)
