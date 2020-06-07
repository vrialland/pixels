from typing import Tuple


def hex2rgb(color: int) -> Tuple[int]:
    return (color >> 16 & 0xFF, color >> 8 & 0xFF, color >> 0 & 0xFF)
