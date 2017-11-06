import asyncio
from aiohttp import web
import aiohttp_jinja2
import jinja2

from routes import routes

loop = asyncio.get_event_loop()

app = web.Application(loop=loop)
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
app.router.add_static('/static', 'static', name='static')

for route in routes:
    app.router.add_route(route[0], route[1], route[2], name=route[3])

web.run_app(app, host='127.0.0.1', port=8080)

# f = loop.create_server(app.make_handler(), '127.0.0.1', 8080)
# srv = loop.run_until_complete(f)
# print('serving on', srv.sockets[0].getsockname())
# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     pass
