import os


# === 1, 2, 3 ТАПСЫРМАЛАР: ЖОЛДАРМЕН ЖҰМЫС ===
def string_tasks():
    print("--- 1. Жолдармен жұмыс (1, 2, 3-тапсырмалар) ---")
    text = input("Мәтін немесе сөйлем енгізіңіз: ").strip()

    # 1. Кері ретпен шығару
    print(f"Кері реттелген мәтін: {text[::-1]}")

    # 2. Сөздер санын анықтау
    words = text.split()
    print(f"Мәтіндегі сөздер саны: {len(words)}")

    # 3. Сөзді алмастыру
    old_word = input("Алмастырылатын сөз: ")
    new_word = input("Жаңа сөз: ")
    print(f"Өңделген мәтін: {text.replace(old_word, new_word)}\n")


# === 4, 5 ТАПСЫРМАЛАР: РЕКУРСИЯ ===
def factorial(n):
    """Рекурсия арқылы факториал есептеу"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Рекурсия арқылы Фибоначчи сандарын табу"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def recursion_tasks():
    print("--- 2. Рекурсия (4, 5-тапсырмалар) ---")
    num = int(input("Факториал үшін сан енгізіңіз: "))
    print(f"{num}! = {factorial(num)}")

    fib_idx = int(input("Фибоначчи реттік нөмірін енгізіңіз: "))
    print(f"{fib_idx}-ші Фибоначчи саны: {fibonacci(fib_idx)}\n")


# === 6, 7, 8 ТАПСЫРМАЛАР: ФАЙЛДАРМЕН ЖҰМЫС ===
def file_tasks():
    print("--- 3. Файлдармен жұмыс (6, 7, 8-тапсырмалар) ---")
    input_file = "input.txt"
    output_file = "output.txt"

    # Сынақ үшін файл жазу
    with open(input_file, "w", encoding="utf-8") as f:
        f.write("Сәлем Python!\nБұл зертханалық жұмыс.\nФайлдарды оқу өте қызықты.\n")

    # 6 & 7. Файлды оқу, жолдар мен сөздерді санау
    line_count = 0
    word_count = 0
    full_text = ""

    print(f"📄 '{input_file}' файлынан оқылған мәтін:")
    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
            line_count += 1
            word_count += len(line.split())
            full_text += line

    print(f"📊 Статистика: Жолдар саны = {line_count}, Сөздер саны = {word_count}")

    # 8. Өңдеп жаңа файлға жазу (Мәтінді бас әріпке айналдыру)
    with open(output_file, "w", encoding="utf-8") as out_file:
        out_file.write(full_text.upper())
    print(f"📝 Өңделген мәтін '{output_file}' файлына жазылды.\n")


if __name__ == "__main__":
    string_tasks()
    recursion_tasks()
    file_tasks()