# завдання 1. списки

def main():
    #початковий список(цілі числа)
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(f"початковий список: {nums}")

    #індексація
    print(f"\nіндекси:")
    print(f"елемент за індексом 2: {nums[2]}")
    print(f"останній елемент (-1): {nums[-1]}")

    #зрізи
    slice1 = nums[1:4]
    slice2 = nums[:3]
    slice3 = nums[1:8:2]  # з кроком 2

    print(f"\nзрізи:")
    print(f"зріз [1:4]: {slice1}")
    print(f"зріз [:3]: {slice2}")
    print(f"зріз з кроком [1:8:2]: {slice3}")

    #мутації (змінюють існуючий список)
    print(f"\nмутації:")

    nums.append(100)
    print(f"після append(100): {nums}")

    nums.insert(2, 25)
    print(f"після insert(2, 25): {nums}")

    nums.remove(40)
    print(f"після remove(40): {nums}")


if __name__ == "__main__":
    main()