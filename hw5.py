#Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
# Модуль содержит функции:
#1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
#2) выводит список всех делителей числа;
#3) выводит самый большой простой делитель числа.
def is_prime(n):
    '''
    :param n: число на вход
    :return: возвращает True, если число простое и False, если  составное
    '''
    if n == 1:
        return False
    for i in range(2,n+1):
        if n % i == 0 and i == n:
            return True
        elif n % i ==0 and i!= n:
            return False



def number_divider(number):
    '''

    :param number: число
    :return: список из делителей
    '''
    list_of_divider = []
    for i in range(2, number+1):
        if number % i == 0:
            list_of_divider.append(i)
    return list_of_divider






def max_divider(n):
    list_max = []
    list_div = number_divider(n)
    for i in list_div:
        if is_prime(i):
            list_max.append(i)
    return max(list_max)

print(max_divider(195))














