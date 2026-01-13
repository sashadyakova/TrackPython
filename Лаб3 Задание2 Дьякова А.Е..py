# TODO Напишите функцию find_common_participants

def find_common_participants(participants1, participants2, separator=','): # separator=',' — символ-разделитель между фамилиями
    participants_list1 = participants1.split(separator)  # разбиваем строки на списки, split = разделить
    participants_list2 = participants2.split(separator)

    # находим общих участников
    common = [] # пустой список для общих участников
    for person in participants_list1:
        if person in participants_list2:
            common.append(person) # eсли человек есть в обеих группах — записываем его в common, append — команда, которая добавляет новый элемент в конец списка.

    # сортируем список по алфавиту
    common.sort()

    return common # верни список общих участников

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

result = find_common_participants(participants_first_group, participants_second_group, "|")
print(result)