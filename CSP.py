
class CSP:
    def __init__(self, row_n, col_n):
        self.row_numbers = row_n
        self.column_numbers = col_n
        self.N = len(row_n)
        self.matrix = [[-1 for _ in range(self.N)] for _ in range(self.N)]

    def solve_matrix(self):
        row_numbers = self.row_numbers
        column_numbers = self.column_numbers
        matrix = self.matrix
        N = self.N
        # print(matrix)

        def check_column(matrix, i_column):
            numbers = column_numbers[i_column]
            cells = []
            n = 0
            number_index = 0
            for row in matrix:
                if row[i_column] == 1:
                    n += 1
                elif row[i_column] == 0 and n > 0:
                    if number_index < len(numbers) and n == numbers[number_index]:
                        cells.append(n)
                        n = 0
                        number_index += 1
                    else:
                        return False
            if n > 0:
                if number_index < len(numbers) and n == numbers[number_index]:
                    cells.append(n)
            result = True
            for i in range(len(cells)):
                if cells[i] > numbers[i]:
                    result = False
                    break

            return len(cells) <= len(numbers) and result

        def check_row(row, i_row):
            numbers = row_numbers[i_row]
            cells = []
            n = 0
            number_index = 0
            for cell in row:
                if cell == 1:
                    n += 1
                elif cell == 0 and n > 0:
                    if number_index < len(numbers) and n == numbers[number_index]:
                        cells.append(n)
                        n = 0
                        number_index += 1
                    else:
                        return False
            if n > 0:
                if number_index < len(numbers) and n == numbers[number_index]:
                    cells.append(n)
            result = True
            for i in range(len(cells)):
                if cells[i] > numbers[i]:
                    result = False
                    break
                else:
                    result = True

            return len(cells) <= len(numbers) and result

        def is_valid_row(row, i_row):
            cells = []
            n = 0
            for cell in row:
                if cell == 1:
                    n += 1
                elif n > 0:
                    cells.append(n)
                    n = 0
            if n > 0:
                cells.append(n)
            return cells == row_numbers[i_row]

        def is_valid_col(matrix, i_column):
            cells = []
            n = 0
            for row in matrix:
                if row[i_column] == 1:
                    n += 1
                elif n > 0:
                    cells.append(n)
                    n = 0
            if n > 0:
                cells.append(n)
            return cells == column_numbers[i_column]

        def solve(matrix, i_row, i_column):
            if i_row == N:
                return all(is_valid_col(matrix, col) for col in range(N))
            if i_column == N:
                return is_valid_row(matrix[i_row], i_row) and solve(matrix, i_row + 1, 0)

            for val in [1, 0]:
                matrix[i_row][i_column] = val
                if check_row(matrix[i_row], i_row) and check_column(matrix, i_column):
                    if solve(matrix, i_row, i_column + 1):
                        return True
                matrix[i_row][i_column] = -1

            return False

        if solve(matrix, 0, 0):
            return matrix
        else:
            return None


def printMatrix(mat):
    if mat:
        string_matrix = [
            "".join('1' if cell == 1 else '0' for cell in row) for row in mat]
        for row in string_matrix:
            print(row)


def main():
    N = int(input())
    row_numbers = [[int(x) for x in input().split(' ')] for i in range(N)]
    column_numbers = [[int(x) for x in input().split(' ')] for i in range(N)]
    m = CSP(row_numbers, column_numbers)
    s = m.solve_matrix()
    printMatrix(s)


main()

if __name__ == 'main':
    main()
