import os

FILE_NAME = "students.txt"


def load_data():
    """Файлдан студенттер тізімін оқу (Деректерді оқу)"""
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    students.append({
                        "name": parts[0],
                        "id": parts[1],
                        "gpa": parts[2]
                    })
    return students


def save_data(students):
    """Студенттер тізімін файлға сақтау"""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for student in students:
            file.write(f"{student['name']},{student['id']},{student['gpa']}\n")


def add_student(students):
    """Жаңа студент қосу функциясы"""
    print("\n--- Жаңа студентті тіркеу ---")
    name = input("Студенттің аты-жөні: ").strip()
    student_id = input("Студент ID (Журнал нөмірі): ").strip()
    gpa = input("Үлгерім көрсеткіші (GPA): ").strip()

    if name and student_id and gpa:
        students.append({"name": name, "id": student_id, "gpa": gpa})
        save_data(students)
        print("🎉 Студент сәтті қосылды және файлға сақталды!")
    else:
        print("❌ Қате: Барлық өрістерді толтыру қажет!")


def display_students(students):
    """Тізімді экранға шығару функциясы"""
    if not students:
        print("\n📭 Тізім бос. Студенттер табылмады.")
        return

    print("\n" + "=" * 45)
    print(f"{'Аты-жөні':<20} | {'ID Нөмірі':<10} | {'GPA':<5}")
    print("=" * 45)
    for s in students:
        print(f"{s['name']:<20} | {s['id']:<10} | {s['gpa']:<5}")
    print("=" * 45)


def search_student(students):
    """Аты-жөні бойынша студентті іздеу"""
    print("\n--- Студент іздеу ---")
    search_name = input("Ізделетін студенттің есімін енгізіңіз: ").strip().lower()
    found = [s for s in students if search_name in s['name'].lower()]

    if found:
        print(f"\n🔍 Табылған студенттер саны: {len(found)}")
        display_students(found)
    else:
        print("❌ Мұндай студент табылмады.")


def sort_students(students):
    """Студенттерді аты бойынша алфавитпен сұрыптау"""
    if not students:
        print("\n📭 Сұрыптайтын ештеңе жоқ, тізім бос.")
        return
    # Сұрыптау алгоритмі
    sorted_list = sorted(students, key=lambda x: x['name'])
    print("\n--- Алфавит бойынша сұрыпталған тізім ---")
    display_students(sorted_list)


def main():
    """Бағдарламаның негізгі басқару мәзірі"""

    students = load_data()

    while True:
        print("\n===== СТУДЕНТТЕР ТІЗІМІ ЖҮЙЕСІ =====")
        print("1. Жаңа студент қосу")
        print("2. Студенттер тізімін көру")
        print("3. Студентті аты бойынша іздеу")
        print("4. Тізімді алфавитпен сұрыптау")
        print("5. Бағдарламадан шығу")

        choice = input("Әрекетті таңдаңыз (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            sort_students(students)
        elif choice == "5":
            print("\n👋 Бағдарлама аяқталды. Сау болыңыз!")
            break
        else:
            print("❌ Қате таңдау! 1-ден 5-ке дейінгі санды енгізіңіз.")


if __name__ == "__main__":
    main()