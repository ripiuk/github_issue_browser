import asyncio

from aiohttp import web
import aiohttp_jinja2

from .parse_github_api import get_repo_main_info, get_repo_labels


def redirect(request, router_name):
    url = request.app.router[router_name].url()
    raise web.HTTPFound(url)


class SendLink(web.View):

    @aiohttp_jinja2.template('chose_repo.html')
    async def get(self):
        print(self.request)

    @aiohttp_jinja2.template('get_info.html')
    async def post(self):
        response = web.HTTPFound('/repo_info')
        data = await self.request.post()
        response.set_cookie('github_repo', data.get('github_repo'))
        return response


class RepoIssuesStats(web.View):

    @aiohttp_jinja2.template('get_info.html')
    async def get(self):
        repo_url = self.request.cookies.get('github_repo')
        result = dict()
        tasks = [get_repo_main_info(repo_url, result), get_repo_labels(repo_url, result)]
        await asyncio.wait(tasks)
        return result

# TODO: add 'sign in' from gitHub, issues tags, messages, chat websocket, add comment from chat, and just logging
