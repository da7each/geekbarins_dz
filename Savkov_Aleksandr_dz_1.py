duration = int(input('Введите количество секунд: '))

if duration < 60:
    seconds = duration
    print(seconds, 'сек')
elif 60 <= duration < 3600:
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, 'мин', seconds, 'сек')
elif 3660 <= duration < 86400:
    hours = duration // 3600
    minutes = duration // 60
    seconds = duration % 60
    print(hours, 'час' ,minutes, 'мин', seconds, 'сек')
else:
    days = duration // 86400
    hours = (duration % 86400) // 3600
    minutes = (duration % 3600) // 60
    seconds = (duration % 60) % 60
    print(days, 'дн', hours, 'час' ,minutes, 'мин', seconds, 'сек')



my_list = []
num = 0
while num <= 1000:
    if num % 2 != 0:
         my_list.append(num ** 3)
    num += 1
print(my_list)

final_sum = 0
for num in my_list:
    check_sum = 0
    for check_num in str(num):
         check_sum += int(check_num)
    if check_sum % 7 == 0:
         final_sum += num
print(final_sum)

final_sum17 = 0
for num in my_list:
     num += 17
     check_sum = 0
     for check_num in str(num):
         check_sum += int(check_num)
     if check_sum % 7 == 0:
         final_sum17 += num
print(final_sum17)



percent = int(input('Введите количество процентов: '))

if percent == 1:
    print(percent, 'процент')
elif 1 < percent <= 4:
    print(percent, 'процента')
else:
    print(percent, 'процентов')