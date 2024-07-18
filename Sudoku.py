def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True


def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0 
                return False
    return True


def main():
    print("Do you want to provide input manually or use the default input inside the code?")
    print("1. Manual Input")
    print("2. Use Default Input")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("Please enter the Sudoku puzzle row-wise, with each row separated by spaces.")
        print("Use '0' for empty cells.")
        sudoku=[]
        for i in range(9):
            row=list(map(int,input("Row{}:".format(i+1)).split()))
            sudoku.append(row)
    elif choice=="2":
        sudoku = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]        
    else:
        print("Invalid Choice.Exiting..😔")
        return
    print("\nSudoku Puzzle:")
    for row in sudoku:
        print(*row)

    if solve_sudoku(sudoku):
        print("\nSolved Sudoku Puzzle:")
        for row in sudoku:
            print(*row)
    else:
        print("\nNo solution found.")
if __name__=="__main__":
    main()                
        