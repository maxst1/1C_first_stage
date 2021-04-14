class Resolver:
    def __init__(self, main_map):
        self.main_map = main_map

    def _check_cols(self):
        for i in range(3):
            if self.main_map[0][i] == self.main_map[1][i] == self.main_map[2][i]:
                return i, True

        return 0, False

    def _check_rows(self):
        for i in range(3):
            if self.main_map[i][0] == self.main_map[i][1] == self.main_map[i][2]:
                return i, True

        return 0, False

    def resolve(self):
        i, b = self._check_cols()
        if b:
            return [0, i, 2, i]

        i, b = self._check_rows()
        if b:
            return [i, 0, i, 2]

        if self.main_map[0][0] == self.main_map[2][2]:
            return [0, 0, 2, 2]

        if self.main_map[0][2] == self.main_map[2][0]:
            return [0, 2, 2, 0]

        return [0, 0, 0, 0]
