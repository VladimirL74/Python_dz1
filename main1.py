numbers = []
digit = 0
for digit in range(1, 1000, 2):
    numbers.append(digit ** 3)
print('Список кубов нечетных чисел: ', list(enumerate(numbers, 1)))
suitable_numbers = []
# проверка суммы цифр каждого числа в списке на кратность 7
for digit in numbers:
    sum_of_numbers = 0
    while digit != 0:
        sum_of_numbers = sum_of_numbers + digit % 10
        digit = digit // 10
    if sum_of_numbers % 7 == 0:
        suitable_numbers.append(sum_of_numbers)
print('Список чисел, сумма цифр которых кратна 7:', list(enumerate(suitable_numbers, 1)))
print('Сумма чисел, кратных 7: ', sum(suitable_numbers))
# прибавление числа 17 ко всем числам в списке
new_numbers = [x + 17 for x in suitable_numbers]
print('Ко всем числам в списке прибавлено 17: ', list(enumerate(new_numbers, 1)))
final_list = []
# проверка суммы цифр новых чисел в списке на кратность 7
for digit in new_numbers:
    add_number = 0
    while digit != 0:
        add_number = add_number + digit % 10
        digit = digit // 10
    if add_number % 7 == 0:
        final_list.append(add_number)
print('Сумма получившихся чисел, кратных 7: ', sum(final_list))
