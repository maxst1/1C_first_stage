from resolver import Resolver
from image_analyzer import ImageAnalyzer


class CLI:

    @staticmethod
    def cli():
        path = input("Введите путь до изображения:\n")
        image_analyzer = ImageAnalyzer()

        image_analyzer.read_image(path)
        print("{} прочитано".format(path))
        image_analyzer.process_xo()

        main_map = image_analyzer.get_map()
        print("Расчет анализатора:\n {}".format(main_map))
        print("0 - пустота, 1 - Х, 2 - О")

        resolver = Resolver(main_map)
        res_points = resolver.resolve()
        print("Ответ алгоритма: {}".format(res_points))

        if image_analyzer.process_output(res_points):
            print("Результат в файле output.pnt")

        print("Done")
