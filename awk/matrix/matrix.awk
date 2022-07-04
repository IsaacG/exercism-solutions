@namespace "matrix"

function read(filename, matrix_var,  _nr) {
    _nr = 0
    while ((getline < filename) > 0) {
        _nr++
        for (i = 1; i <= NF; i++)
            matrix_var[_nr][i] = $i
    }
    close(filename)
}

function row(matrix_var, row_num) {
    for (i = 1; i <= length(matrix_var[row_num]); i++)
        out = out " " matrix_var[row_num][i]
    return substr(out, 2)
}

function column(matrix_var, column_num) {
    for (i = 1; i <= length(matrix_var); i++)
        out = out " " matrix_var[i][column_num]
    return substr(out, 2)
}
