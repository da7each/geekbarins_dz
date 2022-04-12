class Data:
    def __init__(self, data_test):
        self.data_test = str(data_test)

    @classmethod
    def extract(cls, data_test):
        my_date = []
        for i in data_test.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Дата указана верно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.data_test)}'


today = Data('12 - 4 - 2022')

print(today)
print(Data.valid(1, 11, 2020))
print(Data.valid(41, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract('11 - 3 - 2022'))
print(today.extract('10 - 12 - 1999'))




class DivisionByZero:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def division_by_zero(dividend, divider):
        try:
            return (dividend / divider)
        except:
            return (f"Деление на ноль недопустимо")


division = DivisionByZero(100, 10)

print(DivisionByZero.division_by_zero(10, 0))
print(DivisionByZero.division_by_zero(10, 2))
print(division.division_by_zero(100, 0))
print(division.division_by_zero(100, 5))



class Checker:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = input('Введите значения: ')
                if val == 'stop':
                    return f'Скрипт остановлен. \nТекущий список: {self.my_list} \n '
                if not val.isdigit():
                    raise
                self.my_list.append(val)
                print(f'Текущий список: {self.my_list} \n ')
            except:
                print(f"Недопустимое значение, попробуйте ещё раз.")

try_except = Checker(1)
print(try_except.my_input())



class Warehouse:

    def __init__(self, name, price, quantity, sheets, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sheets = sheets
        self.my_store_all = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'модель {self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            model = input(f'Введите наименование: ')
            price = int(input(f'Введите цену за ед: '))
            quantity = int(input(f'Введите количество: '))
            unique = {'Модель устройства': model, 'Цена за ед': price, 'Количество': quantity}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список: {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для завершения введите "stop" , для продолжения нажмите "Enter"')
        stoper = input(f'')
        if stoper == 'stop':
            self.my_store_all.append(self.my_store)
            return f'На складе: {self.my_store_all}'
        else:
            return Warehouse.reception(self)


class Printer(Warehouse):
    def to_print(self):
        return f'Напечатал {self.sheets} листов'

class Scanner(Warehouse):
    def to_scan(self):
        return f'Отсканировал {self.sheets} листов'

class Copier(Warehouse):
    def to_copie(self):
        return f'Копировал {self.sheets} листов'


unit_1 = Printer('HP', 1000, 3, 0)
unit_2 = Scanner('Canon', 1500, 1, 0)
unit_3 = Copier('Xerox', 2000, 1, 10)
print(unit_1.reception())



class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма:')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение:')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a + self.a * other.b} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, 2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)