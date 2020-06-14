import logging

from starlette.applications import Starlette
from starlette.config import Config
from starlette.endpoints import WebSocketEndpoint
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from pixels.screen import Screen

config = Config(".env")
MATRIX_COLS = config("MATRIX_COLS", default=32, cast=int)
MATRIX_ROWS = config("MATRIX_ROWS", default=16, cast=int)

logger = logging.getLogger(__file__)

screen = Screen(MATRIX_COLS, MATRIX_ROWS)


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
        logger.info('Received "%s"', data)
