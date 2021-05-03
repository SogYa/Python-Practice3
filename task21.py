def swap(first, second):                # Такое название аргументов написано в задании
    if len(first) == len(second):
        for i in range(len(first)):
            first[i], second[i] = second[i], first[i]
    elif len(first) > len(second):
        min_len = len(second)                                # Длинна 2 списка в начале должны быть = длинне 1 в конце, записываем в переменную тк потом длины будут меняться и будут ошибки
        for i in range(len(second)):                         # Меняем элементы списков при равных индексах
            first[i], second[i] = second[i], first[i]
        while len(first) != min_len:
            second.append(first[min_len])
            del first[min_len]
    elif len(first) < len(second):
        min_len = len(first)
        for i in range(len(first)):
            first[i], second[i] = second[i], first[i]
        while len(second) != min_len:
            first.append(second[min_len])
            del second[min_len]


first = [4, 5, 6, 7, 44, 23, 231231]
second = [1, 2, 3, 231, 23412, 1111, 22222, 423]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)
