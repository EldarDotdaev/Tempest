numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
#print("Исходный список:",numbers)
#print("Поиск None:","(",sum(numbers[0:numbers.index(None)]),"+",sum(numbers[numbers.index(None)+1:len(numbers)]),")","/",len(numbers),"=",(sum(numbers[0:numbers.index(None)])+sum(numbers[numbers.index(None)+1:len(numbers)]))/len(numbers))
numbers[numbers.index(None)]=(sum(numbers[0:numbers.index(None)])+sum(numbers[numbers.index(None)+1:len(numbers)]))/len(numbers)
print("Измененный список:",numbers)