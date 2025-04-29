
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        """
        添加或更新学生的成绩

        参数:
        subject -- 科目名称
        grade -- 成绩
        """
        self.grades[subject] = grade

    def get_average_grade(self):
        """
        计算学生的平均成绩

        返回:
        平均成绩
        """
        if not self.grades:
            return 0
        total = sum(self.grades.values())
        return total / len(self.grades)

def main():
    students = {}

    def add_student(name):
        students[name] = Student(name)

    def add_grade(name, subject, grade):
        if name in students:
            students[name].add_grade(subject, grade)
        else:
            print(f"学生 {name} 不存在。")

    def print_student_info(name):
        if name in students:
            student = students[name]
            print(f"学生: {student.name}")
            for subject, grade in student.grades.items():
                print(f"{subject}: {grade}")
            print(f"平均成绩: {student.get_average_grade():.2f}")  # .2f--保留两位小数点
        else:
            print(f"学生 {name} 不存在。")

    def menu():
        while True:
            print("\n学生成绩管理系统")
            print("1. 添加学生")
            print("2. 添加成绩")
            print("3. 打印学生信息")
            print("4. 退出")
            choice = input("请选择操作（1/2/3/4）：")

            if choice == '1':
                name = input("请输入学生姓名：")
                add_student(name)
            elif choice == '2':
                name = input("请输入学生姓名：")
                subject = input("请输入科目名称：")
                grade = float(input("请输入成绩："))
                add_grade(name, subject, grade)
            elif choice == '3':
                name = input("请输入学生姓名：")
                print_student_info(name)
            elif choice == '4':
                print("退出系统。")
                break
            else:
                print("无效的选择，请重新输入。")

    menu()

if __name__ == "__main__":
    main()
