class Matrix(object):

    def __init__(self, matrix_string):
        rows = []
        for l in matrix_string.split('\n'):
            rows.append([int(v) for v in l.split(' ')])
        cols = []
        if rows:
            for i in range(len(rows[0])):
                cols.append([r[i] for r in rows])

        self.rows = rows
        self.cols = cols

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.cols[index - 1]

# vim:ts=4:sw=4:expandtab
