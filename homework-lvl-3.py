# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[None] * columns for _ in range(rows)]

    def set_value(self, row, column, value):
        if not (1 <= row <= self.rows) or not (1 <= column <= self.columns):
            raise IndexError("Упс")
        self.matrix[row - 1][column - 1] = value

    def replace_value(self, row, column, value):
        self.set_value(row, column, value)

    def num_rows(self):
        return self.rows

    def num_columns(self):
        return self.columns

    def resize(self, new_rows, new_columns):
        if new_rows < 0 or new_columns < 0:
            raise ValueError("Недопустимый размер")
        new_matrix = [[None] * new_columns for _ in range(new_rows)]
        for i in range(min(self.rows, new_rows)):
            for j in range(min(self.columns, new_columns)):
                new_matrix[i][j] = self.matrix[i][j]
        self.matrix = new_matrix
        self.rows = new_rows
        self.columns = new_columns

    def __str__(self):
        return '\n'.join([' '.join([str(cell) if cell is not None else 'None' for cell in row]) for row in self.matrix])


matrix = Matrix(10, 10)
for i in range(1, 11):
    for j in range(1, 11):
        matrix.set_value(i, j, 1)

print("Number of rows:", matrix.num_rows()) 
print("Number of columns:", matrix.num_columns())
print(matrix)

# Если меняем размеры
matrix.resize(3, 5)

print("Number of rows:", matrix.num_rows())
print("Number of columns:", matrix.num_columns())
print(matrix)