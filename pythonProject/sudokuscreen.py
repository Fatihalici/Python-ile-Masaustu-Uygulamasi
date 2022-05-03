with open(r"sudoku.txt", "r") as my_file:
    lines = my_file.read()
    sudoku = [[character for character in line if not character == " "] for line in lines.split("\n")]
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] != "*":
                sudoku[i][j] = int(sudoku[i][j])
