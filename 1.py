#Рассмотрим три числа
# a
# b
# c Упорядочим их по возрастанию.
# Какое число будет стоять между двумя другими?

arr = input().split()
new_arr = []
for el in arr:
    new_arr.append(int(el))
new_arr.sort()
print(new_arr[1])



