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
        self.canvas = self.matrix.CreateFrameCanvas()

    def clear(self):
        self.canvas.Clear()

    def fill(self, color: int):
        self.canvas.Fill(*hex2rgb(color))

    def set_pixel(self, x: int, y: int, color: int):
        self.canvas.SetPixel(x, y, *hex2rgb(color))

    def draw_circle(self, x: int, y: int, radius: int, color: int):
        color = graphics.Color(*hex2rgb(color))
        graphics.DrawCircle(self.canvas, x, y, radius, color)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: int):
        color = graphics.Color(*hex2rgb(color))
        graphics.DrawLine(self.canvas, x1, y1, x2, y2, color)

    def draw_text(self, x: int, y: int, text: str, color: int):
        color = graphics.Color(*hex2rgb(color))
        font = graphics.Font()
        path = os.path.join(os.path.dirname(__file__), "..", "fonts", "7x13.bdf")
        font.LoadFont(path)
        graphics.DrawText(self.canvas, font, x, y, color, text)

    def update(self):
        self.canvas = self.matrix.SwapOnVSync(self.canvas)
