#!/usr/bin/python3
""" N queens """

import syst


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    placed_queens = []  # Stats out format [row, column]
    stop = False
    r = 0
    c = 0

    # iterate throu rows
    while r < n:
        goback = False
        # iterate throu columns
        while c < n:
            safe = True
            for stat in placed_queens:
                col = stat[1]
                if(col == c or col + (r-stat[0]) == c or
                        col - (r-stat[0]) == c):
                    safe = False
                    break

            if not safe:
                if c == n - 1:
                    goback = True
                    break
                c += 1
                continue

            # initiate the queen
            stats = [r, c]
            placed_queens.append(stats)
            if r == n - 1:
                solutions.append(placed_queens[:])
                for stat in placed_queens:
                    if stat[1] < n - 1:
                        r = stat[0]
                        c = stat[1]
                for i in range(n - r):
                    placed_queens.pop()
                if r == n - 1 and c == n - 1:
                    placed_queens = []
                    stop = True
                r -= 1
                c += 1
            else:
                c = 0
            break
        if stop:
            break
        if goback:
            r -= 1
            while r >= 0:
                c = placed_queens[r][1] + 1
                del placed_queens[r]
                if c < n:
                    break
                r -= 1
            if r < 0:
                break
            continue
        r += 1

    for i, k in enumerate(solutions):
        if i == len(solutions) - 1:
            print(k, end='')
        else:
            print(k)
