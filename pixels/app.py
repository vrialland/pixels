import json
import logging

from starlette.applications import Starlette
from starlette.config import Config
from starlette.endpoints import WebSocketEndpoint
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

logger = logging.getLogger(__file__)

try:
    from pixels.screen import Screen
except:
    logger.error("Cannot load Screen, is `rgbmatrix` lib available?")

    class Screen:
        def __init__(*args, **kwargs):
            pass

        def set_pixel(self, *args, **kwargs):
            pass

        def update(self):
            pass


config = Config(".env")
MATRIX_COLS = config("MATRIX_COLS", default=32, cast=int)
MATRIX_ROWS = config("MATRIX_ROWS", default=16, cast=int)


matrix = Screen(MATRIX_COLS, MATRIX_ROWS)


routes = (Mount("/static", StaticFiles(directory="static")),)
templates = Jinja2Templates(directory="templates")
app = Starlette(debug=True, routes=routes)


@app.route("/")
def index(request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "cols": MATRIX_COLS, "rows": MATRIX_ROWS}
    )


@app.websocket_route("/ws")
class ControlWebsocketEndpoint(WebSocketEndpoint):
    async def on_connect(self, websocket):
        await websocket.accept()

    async def on_disconnect(self, websocket, close_code):
        logger.info("Connection lost")

    async def on_receive(self, websocket, data):
        data = json.loads(data)
        action = data.get("action")
        if action is None:
            return
        logger.info('Received "%s"', action)
        row = int(data["row"])
        col = int(data["col"])
        if action == "set_color":
            color = f"0x{data['color'][1:]}"
            matrix.set_pixel(col, row, int(color, 16))
            logger.info(f"Set color to #{color} on {col},{row}")
        elif action == "reset_color":
            matrix.set_pixel(col, row, 0x000000)
            logger.info(f"Reset color on {col},{row}")
        matrix.update()
