from aiohttp import web

from bot.custom_send import custom_send
from bot.utils import validate_data
from bot_logging import LOG

routes = web.RouteTableDef()


@routes.post('/send-message')
async def handler(request):
    data = await request.json()
    is_valid = validate_data(data)
    if is_valid:
        custom_send(chat_id=data['chat_id'], text=data['text'])
        return web.Response(status=200)
    else:
        err = f'data {data} must contain chat_id and text keys'
        LOG.error(err)
        return web.Response(status=500, body=err)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
