word = input("Сөз енгізіңіз: ")

if word == word[::-1]:
    print("Палиндром")
else:
    print("Палиндром емес")