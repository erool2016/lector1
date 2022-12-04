
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Student(Mentor):
    def __init__(self, name, surname, age):
        super().__init__(name=name, surname =surname)
        self.age = age
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def give_grades_to_lecturers(self, lector, course, grade):
        '''ставлю оценки лекторам'''
        if isinstance(lector, Lector) and course in self.courses_in_progress and  course in lector.courses_attached:
            if course in lector.grades_1:
                lector.grades_1[course] += [grade]
            else:
                lector.grades_1[course] = [grade]
        else:
            print('ошибка')
    def average_grade_st(self):
        '''средняя оценка студента'''
        list_grade_st = []
        for s in self.grades.values():
            for grade in s:
                list_grade_st.append(grade)
        # print(list_grade_st)
        return sum(list_grade_st)/len(list_grade_st)

    def __str__(self):

        return f'Студент\nИмя : {self.name}\nФамилия : {self.surname}\nСредняя оценка за домашние задания :{self.average_grade_st()}\n{self.grades.values()}\nЗавершенные курсы : {self.finished_courses}\nКурсы в процессе изучения :{self.courses_in_progress}'



class Lector(Mentor):

    def __init__(self, name ,surname, academic_degree):
        super().__init__(name=name, surname =surname)
        self.academic_degree = academic_degree
        self.leading_the_course = []
        self.grades_1 = {}

    def average_grade_lector(self):
        '''средняя оценка лектора'''
        lector_av_grade = []
        for list_grade in self.grades_1.values():
            # print(list_grade)
            for grade in list_grade:
                lector_av_grade.append(grade)

        return sum(lector_av_grade)/len(lector_av_grade)

    def __str__(self):
        print(f'Лектор\nИмя : {self.name}\nФамилия : {self.surname}\nСредняя оценка за лекции  {self.average_grade_lector()}')
        # return f'Имя : {self.name}\nФамилия : {self.surname}\nСредняя оценка за лекции {average_rating_student(list_student, "Python")}'

    def __lt__(self, other):
        return self.average_grade_lector() < other
    def __le__(self, other):
        return self.average_grade_lector() <= other

    def __gt__(self, other):
        return self.average_grade_lector() > other

    def __ge__(self, other):
        return self.average_grade_lector() >= other

    def __eq__(self, other):
        return self.average_grade_lector() == other
    def __ne__(self, other):
        return self.average_grade_lector() != other

class Reviewer(Mentor):
    def __init__(self,name ,surname,):
        super().__init__(name=name, surname=surname)
        self.leading_the_course = []

    def give_student_grade(self,student1,courses, grade):
        '''ставлю оценки студентам'''
        if isinstance(student1, Student) and courses in self.leading_the_course and  courses in student1.courses_in_progress:
            if courses in student1.grades:
                student1.grades[courses] += [grade]
            else:
                student1.grades[courses] = [grade]
        else:
            print('ошибка')

    def __str__(self):
        print(f'Проверяющий \nИмя : {self.name}\nФамилия : {self.surname}')
        return f'Имя : {self.name}\nФамилия : {self.surname}'




student_1 = Student('Vova', 'Vovin', '20')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['C']
student_1.grades['Python'] = []
student_1.finished_courses += ['Введение в програмирование']


student_2 = Student('Sergei', 'Sergeev', '20')
student_2.courses_in_progress += ['Python']
student_2.grades['Python'] = []
student_2.finished_courses += ['Введение в програмирование']
student_2.finished_courses += ['Основы програмирования Pyhon']


lector_1 = Lector('Elena','Ivanova', 'list_coursec_lector1')
lector_1.leading_the_course += ['Python']
lector_1.courses_attached += ["Python"]
lector_1.grades_1["Python"] = []
lector_2 = Lector('Ele','Ivanov', 'list_coursec_lector1')
lector_2.leading_the_course += ['Python']
lector_2.courses_attached += ["Python"]
lector_2.grades_1["Python"] = []

student_1.give_grades_to_lecturers(lector_1,'Python', 10)
student_1.give_grades_to_lecturers(lector_1,'Python', 9)
student_1.give_grades_to_lecturers(lector_1,'Python', 9)
student_1.give_grades_to_lecturers(lector_2,'Python', 9)
student_1.give_grades_to_lecturers(lector_2,'Python', 9)

revievr_1 = Reviewer('Sidor','Sidorov')
revievr_1.leading_the_course += ['Python']
revievr_1.give_student_grade(student_1,'Python', 3)
revievr_1.give_student_grade(student_1,'Python', 6)
revievr_1.give_student_grade(student_1,'Python', 9)
revievr_1.give_student_grade(student_2,'Python', 7)
revievr_1.give_student_grade(student_2,'Python', 9)
revievr_1.give_student_grade(student_2,'Python', 10)
revievr_1.give_student_grade(student_2,'Python', 10)
revievr_1.give_student_grade(student_2,'Python', 10)

list_student =[]
list_student += student_1.grades.values()
list_student += student_2.grades.values()
# print('---------' ,list_student)
list_lector = []
list_lector += [lector_1.grades_1.values()]
list_lector += [lector_2.grades_1.values()]
'''функция подсчета средней у студентов'''
def average_rating_student(list_student, course):

    list_grade = []
    for student in list_student:
        for grade in student:
            list_grade.append(grade)
    # print(list_grade)
    # print(sum(list_grade)/len(list_grade),'средняя оценка студентов',list_grade)
    return sum(list_grade)/len(list_grade)


'''Подсчет средней оценки у лесторов'''
def lector_average(list_lector, course):
    list_grade_lector = []
    for lector in list_lector:
        # print(lector)
        for st_course in lector:
            # print(st_course)
            for grade in st_course:
                    # print(grade)
                list_grade_lector.append(grade)
    # print('средняя оценка лектров ',sum(list_grade_lector)/len(list_grade_lector),list_grade_lector)
    return (sum(list_grade_lector) / len(list_grade_lector))


lector_average(list_lector,'Python')
average_rating_student(list_student,'Python')

lector_1.__str__()
lector_2.__str__()
print(lector_average(list_lector,'Python'),' - средняя оценка за лекции у лекторов')
revievr_1.__str__()
print(student_1.__str__())
print(student_2.__str__())
print(average_rating_student(list_student,'Python'))
print(lector_1.average_grade_lector() < lector_2.average_grade_lector())
print(lector_1.average_grade_lector() > lector_2.average_grade_lector())
# print(lector_1.average_grade_lector() <= lector_2.average_grade_lector())
# print(lector_1.average_grade_lector() >= lector_2.average_grade_lector())
print(lector_1.average_grade_lector() == lector_2.average_grade_lector())
print(lector_1.average_grade_lector() != lector_2.average_grade_lector())

