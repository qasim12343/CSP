
class CSP:
    def __init__(self, row_n, col_n):
        self.row_numbers = row_n
        self.column_numbers = col_n
        self.N = len(row_n)
        self.grid = [[-1 for _ in range(self.N)] for _ in range(self.N)]

    def solve_matrix(self):
        row_numbers = self.row_numbers
        column_numbers = self.column_numbers
        grid = self.grid
        N = len(row_numbers)
        # -1 represents unassigned cells
        # grid = [[-1 for _ in range(N)] for _ in range(N)]

        def is_valid_row(row, i_row):
            cells = []
            count = 0
            for cell in row:
                if cell == 1:
                    count += 1
                elif count > 0:
                    cells.append(count)
                    count = 0
            if count > 0:
                cells.append(count)
            return cells == row_numbers[i_row]

        def is_valid_col(grid, i_column):
            cells = []
            count = 0
            for row in grid:
                if row[i_column] == 1:
                    count += 1
                elif count > 0:
                    cells.append(count)
                    count = 0
            if count > 0:
                cells.append(count)
            return cells == column_numbers[i_column]

        def check_row(row, i_row):
            clues = row_numbers[i_row]
            cells = []
            count = 0
            clue_index = 0
            for cell in row:
                if cell == 1:
                    count += 1
                elif cell == 0 and count > 0:
                    if clue_index < len(clues) and count == clues[clue_index]:
                        cells.append(count)
                        count = 0
                        clue_index += 1
                    else:
                        return False
            if count > 0:
                if clue_index < len(clues) and count == clues[clue_index]:
                    cells.append(count)
            return len(cells) <= len(clues) and all(b <= c for b, c in zip(cells, clues))

        def check_column(grid, i_column):
            clues = column_numbers[i_column]
            cells = []
            count = 0
            clue_index = 0
            for row in grid:
                if row[i_column] == 1:
                    count += 1
                elif row[i_column] == 0 and count > 0:
                    if clue_index < len(clues) and count == clues[clue_index]:
                        cells.append(count)
                        count = 0
                        clue_index += 1
                    else:
                        return False
            if count > 0:
                if clue_index < len(clues) and count == clues[clue_index]:
                    cells.append(count)
            return len(cells) <= len(clues) and all(b <= c for b, c in zip(cells, clues))

        def solve(grid, i_row, i_column):
            if i_row == N:
                return all(is_valid_col(grid, col) for col in range(N))
            if i_column == N:
                return is_valid_row(grid[i_row], i_row) and solve(grid, i_row + 1, 0)

            for val in [1, 0]:
                grid[i_row][i_column] = val
                if check_row(grid[i_row], i_row) and check_column(grid, i_column):
                    if solve(grid, i_row, i_column + 1):
                        return True
                grid[i_row][i_column] = -1

            return False

        if solve(grid, 0, 0):
            return grid
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

# N = 10
# row_numbers = [[3, 4], [3, 3], [4], [3, 1], [
#     2, 1, 2], [4, 1], [2, 1, 1], [1, 2], [6], [6]]
# column_numbers = [[5], [7], [4, 1], [3, 5], [2], [
#     1, 4], [1, 3], [2, 3, 2], [2, 1, 2], [2]]

# # 0111001111
# # 0111000111
# # 1111000000
# # 1110000100
# # 1100010110
# # 1111000100
# # 1101010000
# # 0001011000
# # 0001111110
# # 0001111110
# # Solve and format the grid
# m = CSP(row_numbers, column_numbers)
# s = m.solve_matrix()
# printMatrix(s)
