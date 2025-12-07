numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

number_None = numbers[:4]+numbers[5:]
sredznach = sum(number_None)/len(numbers)
numbers[4] = sredznach
print("Измененный список:", numbers)


