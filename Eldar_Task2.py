# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, sep=','):
    list_ = list(set(first.split(sep)).intersection(second.split(sep)))
    list_.sort()
    return list_

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

# TODO Провеьте работу функции с разделителем отличным от запятой
