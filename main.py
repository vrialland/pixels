import time
from pixels import screen

matrix = screen.Screen(32, 16)

matrix.fill(0x222222)

matrix.set_pixel(1, 1, 0xFF0000)

# Rectangle
matrix.draw_line(0, 0, 31, 0, 0x00FF00)
matrix.draw_line(0, 15, 31, 15, 0x00FF00)
matrix.draw_line(0, 0, 0, 15, 0x00FF00)
matrix.draw_line(31, 0, 31, 15, 0x00FF00)
# Text
matrix.draw_text(3, 3, "Hello", 0xFFFFFF)

matrix.draw_circle(16, 8, 4, 0x0000FF)

matrix.update()

time.sleep(10)
