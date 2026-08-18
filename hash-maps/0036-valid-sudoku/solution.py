class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 1. Create one set for every row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # 2. Visit every cell in the board
        for row in range(9):
            for column in range(9):
                value = board[row][column]

                # Empty cells do not affect validity
                if value == ".":
                    continue

                # Convert the cell's position into one of the nine box indexes
                box = (row // 3) * 3 + (column // 3)

                # A repeated value in any of its three regions makes the board invalid
                if (
                    value in rows[row]
                    or value in columns[column]
                    or value in boxes[box]
                ):
                    return False

                # Record the value in its row, column, and box
                rows[row].add(value)
                columns[column].add(value)
                boxes[box].add(value)

        return True
