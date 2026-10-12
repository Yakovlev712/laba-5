a = int(input("Введи количество чисел, которое будешь писать в терминал"))

first_sum = 0 
count = 0 
result_sum = 0 

for i in range (a):
    x = int(input(f"Введи число {i + 1 }: "))
    first_sum += x 

    if i > 0:
        average = first_sum / i 

        if  x > average:
            count += 1
            result_sum += x 

print("КОличество", count)
print("Сумма", result_sum)