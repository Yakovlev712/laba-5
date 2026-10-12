
n = int(input("Введи количество целых чисел, сколько ты будешь вписывать в терминал"))

first_maximum = int(input("Твой первый максимум :"))
count = 0 
result_sum = 0 

for i in range(1 , n):
    x = int(input(f"Введи число {i+1}: "))

    if x > first_maximum:
        count +=1
        result_sum +=x
        first_maximum = x 

print("Количество", count)
print("Сумма", result_sum)