import os

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

from .utils import hex2rgb


class Screen:
    def __init__(self, cols: int, rows: int, **kwargs):
        options = RGBMatrixOptions()
        options.cols = cols
        options.rows = rows
        for k, v in kwargs.items():
            setattr(options, k, v)
        self.matrix = RGBMatrix(options=options)

    def clear(self):
        self.matrix.Clear()

    def fill(self, color: int):
        self.matrix.Fill(*hex2rgb(color))

    def set_pixel(self, x: int, y: int, color: int):
        self.matrix.SetPixel(x, y, *hex2rgb(color))

    def draw_circle(self, x: int, y: int, radius: int, color: int):
        color = graphics.Color(*hex2rgb(color))
        graphics.DrawCircle(self.matrix, x, y, radius, color)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: int):
        color = graphics.Color(*hex2rgb(color))
        graphics.DrawLine(self.matrix, x1, y1, x2, y2, color)

    def draw_text(self, x: int, y: int, text: str, color: int):
        color = graphics.Color(*hex2rgb(color))
        font = graphics.Font()
        path = os.path.join(os.path.dirname(__file__), "..", "fonts", "7x13.bdf")
        font.LoadFont(path)
        graphics.DrawText(self.matrix, font, x, y, color, text)
