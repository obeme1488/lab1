#завдання 2. кортежі

def print_student(student):
    #розпакування кортежу
    name, group, grades = student
    print(f"студент: {name}, група: {group}, оцінки: {grades}")


def calc_average(students):
    #рахуємо середній бал усіх студентів
    total = 0
    count = 0
    for st in students:
        grades = st[2]  #iндекcація(беремо 3-й елемент)
        for g in grades:
            total += g
            count += 1

    if count == 0:
        return 0
    return round(total / count, 2)


def main():
    #список студентів
    students = [
        ("бойко", "кб-1", [90, 85]),
        ("шевченко", "кб-1", [75, 80]),
        ("коваль", "кб-2", [95, 92])
    ]

    print("список студентів:")
    for s in students:
        print_student(s)

    avg = calc_average(students)
    print(f"\nсередній бал: {avg}")

    print("\nперевірка мутабельності:")
    first_st = students[0]

    #пробуємо змінити прізвище (буде помилка)
    try:
        first_st[0] = "вовк"
    except TypeError:
        print("помилка: кортеж не можна змінити")

    #змінюємо вкладений список оцінок
    print("додаємо оцінку першому студенту...")
    first_st[2].append(100)
    print_student(first_st)


if __name__ == "__main__":
    main()