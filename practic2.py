# 1-тапсырма: Тізім ішінен ең үлкен элементті табу (Цикл арқылы)
task1_list = [12, 45, 7, 89, 23]
max_number = task1_list[0]
for num in task1_list:
    if num > max_number:
        max_number = num
print("Ең үлкен элемент:", max_number)

# 2-тапсырма: Тізімдегі сандардың орташа мәнін есептеу
task2_list = [10, 20, 30, 40, 50]
total_sum = sum(task2_list)
average = total_sum / len(task2_list)
print("Орташа мән:", average)

# 3-тапсырма: Сандарды өсу ретімен сұрыптау (sort)
task3_list = [45, 12, 78, 3, 25]
task3_list.sort()  # Тізімді өзінде сұрыптайды
print("Сұрыпталған тізім:", task3_list)
extra_list = [14, 8, 25, 3, 19]
min_number = min(extra_list)
print("Ең кіші сан:", min_number)