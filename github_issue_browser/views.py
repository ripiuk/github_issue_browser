from aiohttp import web
import aiohttp_jinja2


class SendLink(web.View):

    @aiohttp_jinja2.template('chose_repo.html')
    async def get(self):
        pass

    @aiohttp_jinja2.template('get_info.html')
    async def post(self):
        data = await self.request.post()
        return {'github_link': data.get('github_repo')}
