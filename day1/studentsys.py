# 面向对象，学生管理系统
class Student:
    def __init__(self, student_id, student_name, student_grade):
        self.student_id = student_id
        self.student_name = student_name
        self.student_grade = student_grade


class StudentManage:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, student_name, student_grade):
        if student_id in self.students:
            print("该学生已经存在了")
        else:
            self.students[student_id] = Student(student_id, student_name, student_grade)
            print("成功添加")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("删除成功")
        else:
            print("未找到学生")

    def find_student(self, student_id):
        if student_id in self.students:
            student = self.students[student_id]
            print(f"学号: {student.student_id}, 姓名: {student.student_name}, 成绩: {student.student_grade}")
        else:
            print("未找到该学生")

    def find_all_students(self):
        for student_id, student in self.students.items():
            print(f"学号: {student.student_id}, 姓名: {student.student_name}, 成绩: {student.student_grade}")

    def modify_student(self, student_id, student_name, student_grade):
        if student_id in self.students:
            self.students[student_id].student_name = student_name
            self.students[student_id].student_grade = student_grade
        else:
            print("未找到该学生")


def main():
    system = StudentManage()
    while True:
        print("Student Management System")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 查找学生")
        print("4. 展示所有学生")
        print("5. 修改学生")
        print("6. 退出")
        choice = input("输入你的选择：")

        if choice == '1':
            student_id = input("请输入学号")
            name = input("请输入名字")
            grade = input("请输入成绩")
            system.add_student(student_id, name, grade)
        elif choice == '2':
            student_id = input("请输入学号：")
            system.delete_student(student_id)
        elif choice == '3':
            student_id = input("请输入学号")
            system.find_student(student_id)
        elif choice == '4':
            system.find_all_students()
        elif choice == '5':
            student_id = input("请输入学号")
            student_name = input("请输入名字")
            student_grade = input("请输入成绩")
            system.modify_student(student_id, student_name, student_grade)
        elif choice == '6':
            print("成功退出")
            break
        else:
            print("输入错误，请重试！")


if __name__ == "__main__":
    main()