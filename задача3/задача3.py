
#3) Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

def sum_digits(num):
    return sum(map(int, num.replace('.','').replace('-','')))

num = input('Введите число: ')
print(f'Сумма цифр в этом числе равна {sum_digits(num)}')
