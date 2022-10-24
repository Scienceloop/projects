def spiralPrint(mCols, nRows, arr):
    starting_row_index = 0
    starting_column_index = 0

    while (starting_row_index < mCols and starting_column_index < nRows):

        for i in range(starting_column_index, nRows):
            print(arr[starting_row_index][i], end=" ")

        starting_row_index += 1

        for i in range(starting_row_index, mCols):
            print(arr[i][nRows - 1], end=" ")

        nRows -= 1

        if (starting_row_index < mCols):

            for i in range(nRows - 1, (starting_column_index - 1), -1):
                print(arr[mCols - 1][i], end=" ")

            mCols -= 1

        if (starting_column_index < nRows):
            for i in range(mCols - 1, starting_row_index - 1, -1):
                print(arr[i][starting_column_index], end=" ")

            starting_column_index += 1


a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

R = 4
C = 4

spiralPrint(R, C, a)

