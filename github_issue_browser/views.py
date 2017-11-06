from aiohttp import web
import aiohttp_jinja2


class SendLink(web.View):

    @aiohttp_jinja2.template('chose_repo.html')
    async def get(self):
        pass

    @aiohttp_jinja2.template('get_info.html')
    async def post(self):
        data = await self.request.post()
        for smth in data:
            print(smth)
        print('data:', data)
