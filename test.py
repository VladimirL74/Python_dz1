digits = []
digit = 0
for digit in range(1, 1000, 2):
    digits.append(digit ** 3)
print('Список кубов нечетных чисел: ', digits)
good_digits = []

for digit in range(len(digits)):
    sum_number = 0
    while digit != 0:
        sum_number = sum_number + digit % 10
        digit = digit // 10
    if sum_number % 7 == 0:
        digits.append(sum_number)

print('Список чисел, сумма цифр которых кратна 7:', digits)
for i in range(len(digits)):
    sum = 0
    while i >= len(digits):
        sum = sum + i % 10
        i = i // 10
    if sum % 7 == 0:
        digits.append(sum)
print('Список чисел,:', digits)
s = 0
for x in digits:
    if x % 2 == 0:
        s += x
print(x)
