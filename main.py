from random import randint as Ri
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and
                course in lecturer.courses_attached):
            if course in lecturer.rating:
                lecturer.rating[course] += [rate]
            else:
                lecturer.rating[course] = [rate]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_list = []
        for grade in self.grades.values():
            grades_list += grade
        average_grade = str(sum(grades_list) / len(grades_list))
        return average_grade
            
    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Не корректное сравнение!'
        else:
            if self.average_grade() > other.average_grade():
                return f'Студент {self.name} {self.surname} успешнее, чем {other.name} {other.surname}\n'
            else:
                return f'Студент {other.name} {other.surname} успешнее, чем {self.name} {self.surname}\n'
    
    def __str__(self):
        count = 0
        for i in self.grades:
            count += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / count
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.average_rating}\nКурсы в процессе обучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, rate):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [rate]
            else:
                student.grades[course] = [rate]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) # берем значения от родителя 
        self.rating = {}

    def average_rate(self):
        rates_list = []
        for rate in self.rating.values():
            rates_list += rate
        average_rate = str(sum(rates_list) / len(rates_list))
        return average_rate

    def __str__(self):
        return (f'Лектор \nИмя: {self.name} \nФамилия: {self.surname}'\
                f'\nСредняя оценка за лекции: {self.average_rate()}\n')
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не корректное сравнение!')
            return
        else:
            if self.average_rate() > other.average_rate():
                return f'Лектор {self.name} {self.surname} успешнее, чем {other.name} {other.surname}\n'
            else:
                return f'Лектор {other.name} {other.surname} успешнее, чем {self.name} {self.surname}\n'
    

class Reviewer(Mentor): 
    def rate_hw(self, student, course, rate): # выставялем оценки студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [rate]
            else:
                student.grades[course] = [rate]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Проверяющий  - Имя: {self.name}\nФамилия: {self.surname}'
        return res

     
#! Лекторы
lecturer1 = Lecturer('Олег', 'Булыгин')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Алан', 'Тьюринг')
lecturer2.courses_attached += ['Вычислительные машины и разум']

#! Менторы
code_reviewer1 = Reviewer('Линус', 'Торвальдс')
code_reviewer1.courses_attached += ['Python', 'Вычислительные машины и разум']

code_reviewer2 = Reviewer('Кевин', 'Митник')
code_reviewer2.courses_attached += ['Java','Python', 'Вычислительные машины и разум', 'Хаккинг без границ']

#! Студены
student1 = Student('Билл', 'Гейтс', 'male')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Windows для чайников']

student2 = Student('Стив', 'Джобс', 'male')
student2.courses_in_progress += ['Вычислительные машины и разум']
student2.finished_courses += ['Установка hackintosh для начинающих']

#! выставляем оценки лекторам
student1.rate_lecturer (lecturer1, 'Python', Ri(0,10))
student2.rate_lecturer (lecturer2, 'Вычислительные машины и разум', Ri(0,10))
student2.rate_lecturer (lecturer2, 'Вычислительные машины и разум', Ri(0,10))

#! выставляем оценки студентам за домашку

code_reviewer1.rate_hw(student1,'Python', Ri(0,10))
code_reviewer1.rate_hw(student1,'Python', Ri(0,10))
code_reviewer1.rate_hw(student1,'Python', Ri(0,10))
code_reviewer2.rate_hw(student2,'Вычислительные машины и разум', Ri(0,10))
code_reviewer2.rate_hw(student2,'Вычислительные машины и разум', Ri(0,10))
code_reviewer2.rate_hw(student2,'Вычислительные машины и разум', Ri(0,10))

print (student1)
print (student2)
print (lecturer1)
print (lecturer2)
print (code_reviewer1)
print (code_reviewer2)
print (student1 > student2)
print (lecturer2 < student2)
print (lecturer2 > lecturer1)

def avg_grades_all(students_list, course):
    all_grades_list = []
    for student in students_list:
        if student.grades.get(course) is not None:
            all_grades_list += student.grades.get(course)
    all_grades_avg = str(round(sum(all_grades_list) / len(all_grades_list),1))
    print(f'Средняя оценка студентов за домашние задания по курсу {course}: {all_grades_avg}')

def avg_rates_all(lecturer_list, course):
    all_rates_list = []
    for lecturer in lecturer_list:
        if lecturer.rating.get(course) is not None:
            all_rates_list += lecturer.rating.get(course)
    all_rates_avg = str(round(sum(all_rates_list) / len(all_rates_list),1))
    print(f'Средняя оценка всех лекторов в рамках курса {course}: {all_rates_avg}')


avg_grades_all([student1, student2], 'Python')
avg_grades_all([student1, student2], 'Вычислительные машины и разум')

avg_rates_all([lecturer1, lecturer2], 'Python')
avg_rates_all([lecturer1, lecturer2], 'Вычислительные машины и разум')
