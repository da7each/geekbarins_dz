print(type(15*3))
print(type(15/3))
print(type(15//3))
print(type(15**3))


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for elem in my_list:
    if elem.isdigit():
            new_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
            new_list.extend(['"', f'{elem[0]}{int(elem[1:]):02}','"'])
    else:
            new_list.append(elem)

print(' '.join(my_list))
print(' '.join(new_list))


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for position in my_list:
    print('Привет,', position.split()[-1].title())


goods_list = [12, 18.55, 98, 56, 33.30, 99, 83.25, 10, 66, 11.60]
for goods in goods_list:
    r = int(goods)
    kk = (goods - int(goods)) * 100
    print(f'{r} руб {kk:02.0f} коп', end=', ')


goods_list.sort()
print()
for goods in goods_list:
    r = int(goods)
    kk = (goods - int(goods)) * 100
    print(f'{r} руб {kk:02.0f} коп', end=', ')


print()
for elem in reversed(goods_list):
    r = int(elem)
    kk = (elem - int(elem)) * 100
    print(f'{r} руб {kk:02.0f} коп', end=', ')

print()
print(sorted(goods_list)[::-1][:5])





