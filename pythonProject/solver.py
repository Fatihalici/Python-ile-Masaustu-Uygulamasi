import sudokuscreen

from timeit import default_timer as timer

solved1 = False
solved2 = False
solved3 = False
solved4 = False
solved5 = False
solved6 = False
solved7 = False
solved8 = False
solved9 = False
solved10 = False
timecount5 = []
timecount10 = []
timecounter = 0
timecountbeginning = 0
timecountend = 0
boxcount = []
count = 0


def checker(satır, sütun, num):
    # satır ve sütun kontrölleri
    if satır < 6:
        if sütun < 9:
            for j in range(9):
                if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                    return False
            for j in range(9):
                if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                    return False
        else:
            for j in range(9, 18):
                if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                    return False
            for j in range(9):
                if j < 6:
                    if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                        return False
                else:
                    if sudokuscreen.sudoku[j][sütun + 3] == num and sudokuscreen.sudoku[j][sütun + 3] != '*':
                        return False

    elif 6 <= satır <= 8:
        if sütun < 9:
            for j in range(9):
                if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                    return False
            for j in range(9):
                if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                    return False
            if 6 <= sütun <= 8:
                for j in range(6, 15):
                    if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                        return False
                for j in range(6, 15):
                    if 9 <= j <= 11:
                        if sudokuscreen.sudoku[j][sütun - 6] == num and sudokuscreen.sudoku[j][sütun - 6] != '*':
                            return False
                    else:
                        if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                            return False
        elif 9 <= sütun <= 11:
            for j in range(6, 15):
                if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                    return False
            for j in range(6, 15):
                if 9 <= j <= 11:
                    if sudokuscreen.sudoku[j][sütun - 6] == num and sudokuscreen.sudoku[j][sütun - 6] != '*':
                        return False
                else:
                    if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                        return False
        else:
            if sütun <= 14:
                for j in range(6, 21):
                    if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                        return False
                for j in range(0, 15):
                    if j < 6:
                        if sudokuscreen.sudoku[j][sütun - 3] == num and sudokuscreen.sudoku[j][sütun - 3] != '*':
                            return False
                    elif 9 <= j <= 11:
                        if sudokuscreen.sudoku[j][sütun - 6] == num and sudokuscreen.sudoku[j][sütun - 6] != '*':
                            return False
                    else:
                        if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                            return False
            else:
                for j in range(12, 21):
                    if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                        return False
                for j in range(9):
                    if j < 6:
                        if sudokuscreen.sudoku[j][sütun - 3] == num and sudokuscreen.sudoku[j][sütun - 3] != '*':
                            return False
                    else:
                        if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                            return False
    elif 9 <= satır <= 11:
        for j in range(9):
            if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                return False
        for j in range(6, 15):
            if 9 <= j <= 11:
                if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                    return False
            else:
                if sudokuscreen.sudoku[j][sütun + 6] == num and sudokuscreen.sudoku[j][sütun + 6] != '*':
                    return False
    elif 12 <= satır <= 14:
        if sütun < 6:
            for j in range(9):
                if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                    return False
            for j in range(12, 21):
                if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                    return False
        elif 6 <= sütun <= 8:
            for j in range(0, 15):
                if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                    return False
            for j in range(6, 21):
                if 9 <= j <= 11:
                    if sudokuscreen.sudoku[j][sütun - 6] == num and sudokuscreen.sudoku[j][sütun - 6] != '*':
                        return False
                else:
                    if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                        return False
        elif 9 <= sütun <= 11:
            for j in range(6, 15):
                if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                    return False
            for j in range(6, 15):
                if 9 <= j <= 11:
                    if sudokuscreen.sudoku[j][sütun - 6] == num and sudokuscreen.sudoku[j][sütun - 6] != '*':
                        return False
                else:
                    if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                        return False
        elif 12 <= sütun <= 14:
            for j in range(6, 21):
                if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                    return False
            for j in range(6, 21):
                if j > 14:
                    if sudokuscreen.sudoku[j][sütun - 3] == num and sudokuscreen.sudoku[j][sütun - 3] != '*':
                        return False
                elif 9 <= j <= 11:
                    if sudokuscreen.sudoku[j][sütun - 6] == num and sudokuscreen.sudoku[j][sütun - 6] != '*':
                        return False
                else:
                    if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                        return False
        else:
            for j in range(12, 21):
                if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                    return False
            for j in range(12, 21):
                if j > 14:
                    if sudokuscreen.sudoku[j][sütun - 3] == num and sudokuscreen.sudoku[j][sütun - 3] != '*':
                        return False
                else:
                    if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                        return False
    else:
        if sütun < 9:
            for j in range(9):
                if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                    return False
            for j in range(12, 21):
                if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                    return False
        else:
            for j in range(9, 18):
                if sudokuscreen.sudoku[satır][j] == num and sudokuscreen.sudoku[satır][j] != '*':
                    return False
            for j in range(12, 21):
                if j < 15:
                    if sudokuscreen.sudoku[j][sütun + 3] == num and sudokuscreen.sudoku[j][sütun + 3] != '*':
                        return False
                else:
                    if sudokuscreen.sudoku[j][sütun] == num and sudokuscreen.sudoku[j][sütun] != '*':
                        return False

    # 3x3 sudoku kontröl
    for i in range(satır - (satır % 3), satır + 3 - (satır % 3)):
        for j in range(sütun - (sütun % 3), sütun + 3 - (sütun % 3)):
            if sudokuscreen.sudoku[i][j] == num:
                return False
    return True


def solvesudoku_lefttop(f):
    global solved1
    global count
    global timecountbeginning
    global timecountend
    global timecounter
    global boxcount
    for i in range(9):
        for j in range(9):
            if sudokuscreen.sudoku[i][j] == '*':
                for k in range(1, 10):
                    if checker(i, j, k):
                        sudokuscreen.sudoku[i][j] = k
                        solvesudoku_lefttop(f)
                        if solved1 == True:
                            count += 1
                            boxcount.append(count)
                            timecountend += timer()
                            timecounter = timecountend - timecountbeginning
                            timecount10.append(timecounter)
                            f.write(str(i) + str(j) + str(k) + "\n")
                            return
                        sudokuscreen.sudoku[i][j] = '*'
                return
    solved1 = True


def solvesudoku_righttop(f):
    global solved2
    global count
    global timecountbeginning
    global timecountend
    global timecounter
    global boxcount
    for i in range(9):
        for j in range(9, 18):
            if i > 5:
                m = j
                m += 3
                if sudokuscreen.sudoku[i][m] == '*':
                    for k in range(1, 10):
                        if checker(i, m, k):
                            sudokuscreen.sudoku[i][m] = k
                            solvesudoku_righttop2(f)
                            if solved2 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount5.append(timecounter)
                                timecount10.append(timecounter)
                                f.write(str(i) + str(m) + str(k) + "\n")
                                return
                            sudokuscreen.sudoku[i][m] = '*'
                    return
            else:
                if sudokuscreen.sudoku[i][j] == '*':
                    for k in range(1, 10):
                        if checker(i, j, k):
                            sudokuscreen.sudoku[i][j] = k
                            solvesudoku_righttop(f)
                            if solved2 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount10.append(timecounter)
                                f.write(str(i) + str(j) + str(k) + "\n")
                                return
                            sudokuscreen.sudoku[i][j] = '*'
                    return
    solved2 = True


def solvesudoku_mid(f):
    global solved3
    global count
    global timecountbeginning
    global timecountend
    global timecounter
    global boxcount
    for i in range(6, 15):
        for j in range(6, 15):
            if 9 <= i <= 11:
                m = j
                m -= 6
                if sudokuscreen.sudoku[i][m] == '*':
                    for k in range(1, 10):
                        if checker(i, m, k):
                            sudokuscreen.sudoku[i][m] = k
                            solvesudoku_mid(f)
                            if solved3 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount10.append(timecounter)
                                f.write(str(i) + str(m) + str(k) + "\n")
                                return
                            sudokuscreen.sudoku[i][m] = '*'
                    return
            else:
                if sudokuscreen.sudoku[i][j] == '*':
                    for k in range(1, 10):
                        if checker(i, j, k):
                            sudokuscreen.sudoku[i][j] = k
                            solvesudoku_mid(f)
                            if solved3 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount10.append(timecounter)
                                f.write(str(i) + str(j) + str(k) + "\n")
                                return
                            sudokuscreen.sudoku[i][j] = '*'
                    return
    solved3 = True


def solvesudoku_leftbottom(f):
    global solved4
    global count
    global timecountbeginning
    global timecountend
    global timecounter
    global boxcount
    for i in range(12, 21):
        for j in range(9):
            if sudokuscreen.sudoku[i][j] == '*':
                for k in range(1, 10):
                    if checker(i, j, k):
                        sudokuscreen.sudoku[i][j] = k
                        solvesudoku_leftbottom(f)
                        if solved4 == True:
                            count += 1
                            boxcount.append(count)
                            timecountend += timer()
                            timecounter = timecountend - timecountbeginning
                            timecount10.append(timecounter)
                            f.write(str(i) + str(j) + str(k) + "\n")
                            return
                        sudokuscreen.sudoku[i][j] = '*'
                return
    solved4 = True


def solvesudoku_rightbottom(f):
    global solved5
    global count
    global timecountbeginning
    global timecountend
    global timecounter
    global boxcount
    for i in range(12, 21):
        for j in range(9, 18):
            if i < 15:
                m = j
                m += 3
                if sudokuscreen.sudoku[i][m] == '*':
                    for k in range(1, 10):
                        if checker(i, m, k):
                            sudokuscreen.sudoku[i][m] = k
                            solvesudoku_rightbottom(f)
                            if solved5 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount10.append(timecounter)
                                f.write(str(i) + str(m) + str(k) + "\n")
                                return
                            sudokuscreen.sudoku[i][m] = '*'
                    return
            else:
                if sudokuscreen.sudoku[i][j] == '*':
                    for k in range(1, 10):
                        if checker(i, j, k):
                            sudokuscreen.sudoku[i][j] = k
                            solvesudoku_rightbottom(f)
                            if solved5 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount10.append(timecounter)
                                f.write(str(i) + str(j) + str(k) + "\n")
                                return
                            sudokuscreen.sudoku[i][j] = '*'
                    return
    solved5 = True


def solvesudoku_lefttop2(f):
    global solved1
    global count
    global timecountbeginning
    global timecountend
    global timecounter
    global boxcount
    for i in reversed(range(9)):
        for j in reversed(range(9)):
            if sudokuscreen.sudoku[i][j] == '*':
                for k in range(1, 10):
                    if checker(i, j, k):
                        sudokuscreen.sudoku[i][j] = k
                        solvesudoku_lefttop2(f)
                        if solved1 == True:
                            count += 1
                            boxcount.append(count)
                            timecountend += timer()
                            timecounter = timecountend - timecountbeginning
                            timecount5.append(timecounter)
                            timecount10.append(timecounter)
                            f.write(str(i) + str(j) + str(k) + "\n")
                            return
                        sudokuscreen.sudoku[i][j] = '*'
                return
    solved1 = True


def solvesudoku_righttop2(f):
    global solved2
    global count
    global boxcount
    global timecountbeginning
    global timecountend
    global timecounter
    for i in reversed(range(9)):
        for j in reversed(range(9, 18)):
            if i > 5:
                m = j
                m += 3
                if sudokuscreen.sudoku[i][m] == '*':
                    for k in range(1, 10):
                        if checker(i, m, k):
                            sudokuscreen.sudoku[i][m] = k
                            solvesudoku_righttop2(f)
                            if solved2 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount5.append(timecounter)
                                timecount10.append(timecounter)
                                f.write(str(i) + str(m) + str(k) + "\n")
                                return
                            sudokuscreen.sudoku[i][m] = '*'
                    return
            else:
                if sudokuscreen.sudoku[i][j] == '*':
                    for k in range(1, 10):
                        if checker(i, j, k):
                            sudokuscreen.sudoku[i][j] = k
                            solvesudoku_righttop2(f)
                            if solved2 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount5.append(timecounter)
                                timecount10.append(timecounter)
                                f.write(str(i) + str(j) + str(k) + "\n")
                                return
                            sudokuscreen.sudoku[i][j] = '*'
                    return
    solved2 = True


def solvesudoku_mid2(f):
    global solved3
    global count
    global boxcount
    global timecountbeginning
    global timecountend
    global timecounter
    for i in reversed(range(6, 15)):
        for j in reversed(range(6, 15)):
            if 9 <= i <= 11:
                m = j
                m -= 6
                if sudokuscreen.sudoku[i][m] == '*':
                    for k in range(1, 10):
                        if checker(i, m, k):
                            sudokuscreen.sudoku[i][m] = k
                            solvesudoku_mid2(f)
                            if solved3 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount5.append(timecounter)
                                timecount10.append(timecounter)
                                f.write(str(i) + str(m) + str(k) + "\n")
                                return
                            sudokuscreen.sudoku[i][m] = '*'
                    return
            else:
                if sudokuscreen.sudoku[i][j] == '*':
                    for k in range(1, 10):
                        if checker(i, j, k):
                            sudokuscreen.sudoku[i][j] = k
                            solvesudoku_mid2(f)
                            if solved3 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount5.append(timecounter)
                                timecount10.append(timecounter)
                                f.write(str(i) + str(j) + str(k) + "\n")

                                return
                            sudokuscreen.sudoku[i][j] = '*'
                    return
    solved3 = True


def solvesudoku_leftbottom2(f):
    global solved4
    global count
    global boxcount
    global timecountbeginning
    global timecountend
    global timecounter
    for i in reversed(range(12, 21)):
        for j in reversed(range(9)):
            if sudokuscreen.sudoku[i][j] == '*':
                for k in range(1, 10):
                    if checker(i, j, k):
                        sudokuscreen.sudoku[i][j] = k
                        solvesudoku_leftbottom2(f)
                        if solved4 == True:
                            count += 1
                            boxcount.append(count)
                            timecountend += timer()
                            timecounter = timecountend - timecountbeginning
                            timecount5.append(timecounter)
                            timecount10.append(timecounter)
                            f.write(str(i) + str(j) + str(k) + "\n")
                            return
                        sudokuscreen.sudoku[i][j] = '*'
                return
    solved4 = True


def solvesudoku_rightbottom2(f):
    global solved5
    global count
    global boxcount
    global timecountbeginning
    global timecountend
    global timecounter
    for i in reversed(range(12, 21)):
        for j in reversed(range(9, 18)):
            if i < 15:
                m = j
                m += 3
                if sudokuscreen.sudoku[i][m] == '*':
                    for k in range(1, 10):
                        if checker(i, m, k):
                            sudokuscreen.sudoku[i][m] = k
                            solvesudoku_rightbottom2(f)
                            if solved5 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount5.append(timecounter)
                                timecount10.append(timecounter)
                                f.write(str(i) + str(m) + str(k) + "\n")
                                return
                            sudokuscreen.sudoku[i][m] = '*'
                    return
            else:
                if sudokuscreen.sudoku[i][j] == '*':
                    for k in range(1, 10):
                        if checker(i, j, k):
                            sudokuscreen.sudoku[i][j] = k
                            solvesudoku_rightbottom2(f)
                            if solved5 == True:
                                count += 1
                                boxcount.append(count)
                                timecountend += timer()
                                timecounter = timecountend - timecountbeginning
                                timecount5.append(timecounter)
                                timecount10.append(timecounter)
                                f.write(str(i) + str(j) + str(k) + "\n")
                                return
                            sudokuscreen.sudoku[i][j] = '*'
                    return
    solved5 = True
    print(sudokuscreen.sudoku)
