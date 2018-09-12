# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


# coding=utf-8
def my_round(number, ndigits):
    number = number * (10 ** ndigits)
    if float(number) - int(number) > 0.5:
        number = number // 1 + 1
    else:
        number = number // 1
    return number / (10 ** ndigits)

pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


# coding=utf-8
def lucky_ticket(ticket_number):
    n = str(ticket_number)
    a = int(n[0]) + int(n[1])
    b = int(n[-1]) + int(n[-2])

    if a == b:
        return True
    else:
        return False
pass

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))