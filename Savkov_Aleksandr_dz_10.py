class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = []
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Сложение невозможно'

                sum_line = [x + y for x, y in zip(line_1, line_2)]
                answer.append(sum_line)
        else:
            return 'Сложение невозможно'
        return Matrix(answer)

Matrix_1 = Matrix([[1, 2], [3,4], [5,6], [7,8]])
Matrix_2 = Matrix([[1, 2], [3,4], [5,6], [7,8]])
print(Matrix_1 + Matrix_2)


from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calc(self):
        pass

class Coat(Clothes):

    @property
    def calc(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calc(self):
        return round((2 * self.param) + 0.3)


coat = Coat(100)
suit = Suit(100)
print(coat.calc)
print(suit.calc)


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Вычитание невозможно'

    def __mul__(self, other):
        return str(self.nums * other.nums)

    def __floordiv__(self, other):
        return str(self.nums // other.nums)

    def __truediv__(self, other):
        return str(round(self.nums / other.nums))

cell_1 = Cell(10)
cell_2 = Cell(20)
print(cell_2.make_order(5))