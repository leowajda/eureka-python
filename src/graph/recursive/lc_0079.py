from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows, self.cols = len(board), len(board[0])
        self.board = board

        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtrack(row, col, word):
                    return True

        return False

    def backtrack(self, row: int, col: int, word: str) -> bool:

        if len(word) == 0:
            return True

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False

        if self.board[row][col] != word[0]:
            return False

        self.board[row][col] = '#'

        result = False
        for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if self.backtrack(row + row_offset, col + col_offset, word[1:]):
                result = True
                break

        self.board[row][col] = word[0]
        return result
