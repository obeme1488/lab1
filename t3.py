#завдання 3. словник частот

def main():
    print("введіть текст (для завершення введіть 'stop'):")

    freq = {}

    while True:
        line = input("> ")
        if line.lower() == 'stop':
            break

        #розбиваємо рядок на слова
        words = line.split()

        for w in words:
            #нормалізація: малі літери та видалення знаків
            clean_w = w.lower().strip(".,!?")
            if clean_w:
                #безпечне додавання частоти через get
                freq[clean_w] = freq.get(clean_w, 0) + 1

    print("\n--- результати ---")

    #сортування за ключем (за алфавітом)
    print("\nсортування за алфавітом:")
    for k, v in sorted(freq.items()):
        print(f"{k}: {v}")

    #сортування за спаданням частоти (x[1] означає сортувати за значенням)
    print("\nсортування за частотою:")
    for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"{k}: {v}")

    #dict comprehension: слова, які зустрічаються більше 1 разу
    freq_filtered = {k: v for k, v in freq.items() if v > 1}
    print(f"\nчерез comprehension (частота > 1): {freq_filtered}")


if __name__ == "__main__":
    main()