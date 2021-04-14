import numpy as np
import cv2


class ImageAnalyzer:
    def __init__(self):
        self.map = np.zeros((3, 3))

    def _process_properties(self):
        horizontal = self.image.sum(axis=0) != 0
        vertical = self.image.sum(axis=1) != 0

        self.left = horizontal.argmax()
        self.top = vertical.argmax()
        self.height = len(self.image) - vertical[::-1].argmax() - self.top
        self.width = len(self.image[0]) - horizontal[::-1].argmax() - self.left
        self.hor_bin = self.width / 3
        self.vert_bin = self.height / 3

    def _process_rectangle(self, x, y):
        if self.image[x][y]:  # X
            return 1

        for i in np.arange(int(x - (self.hor_bin / 2 - 10)), int(x + (self.hor_bin / 2 - 10))):  # O
            if self.image[i][y]:
                return 2

        return 0

    def _process_map(self):
        for i in range(3):
            for j in range(3):
                x = int(self.top + self.vert_bin * (i + 1 / 2))
                y = int(self.left + self.hor_bin * (j + 1 / 2))
                self.map[i][j] = self._process_rectangle(x, y)

    def read_image(self, path):
        self.origin_image = cv2.imread(path)
        gray_image = cv2.cvtColor(self.origin_image, cv2.COLOR_BGR2GRAY)
        ret, threshold_image = cv2.threshold(gray_image, 127, 1, 0)

        self.image = 1 - threshold_image

    def process_xo(self):
        self._process_properties()
        self._process_map()

    def get_map(self):
        return self.map.copy()

    def get_image_copy(self):
        return self.image.copy()

    def process_output(self, res_points):
        y1, x1, y2, x2 = res_points
        if x1 == y1 == x2 == y2:
            print("There is no winner")
            return False

        x1 = int(self.left + self.hor_bin * (x1 + 1 / 2))
        y1 = int(self.top + self.vert_bin * (y1 + 1 / 2))

        x2 = int(self.left + self.hor_bin * (x2 + 1 / 2))
        y2 = int(self.top + self.vert_bin * (y2 + 1 / 2))

        output = self.origin_image.copy()
        cv2.line(output, (x1, y1), (x2, y2), (0, 0, 0), 10)
        cv2.imwrite("output.png", output)
        return True
