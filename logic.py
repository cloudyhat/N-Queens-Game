class Solution:
    def nqueens(self, n):
        board = [ ["."] * n for _ in range(n)]
        ans = []
        def backtrack(row, col):
            r = row
            c = col

            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1
            row = r
            col = c
            while col >= 0:
                if board[row][col] == "Q":
                    return False
                col -= 1
            row = r
            col = c
            while row < n and col >= 0:
                if board[row][col] == "Q":
                    return False
                row += 1
                col -= 1

            return True
        def solver(col):
            if col == n:
                solution = ["".join(row) for row in board]
                ans.append(solution)
                return
            for row in range(n):
                if backtrack(row, col):
                    board[row][col] = "Q"
                    solver(col + 1)
                    board[row][col] = "."
        solver(0)
        return ans
        
if __name__ == '__main__':
    n = int(input("Enter the value of N : "))
    solution = Solution()
    answer = solution.nqueens(n)
    print("The number of solutions: ", len(answer))
    for sol in answer:
        for row in sol:
            print(row)
        print()