import aiohttp
from yarl import URL
import json


URL_MAIN_INFO = 'https://api.github.com/repos'


async def get_repo_info(repo_url: str) -> dict:
    # Prepare the url
    repo_url = URL(repo_url)
    user_and_repo = repo_url.path
    api_repo_url = URL_MAIN_INFO+user_and_repo

    # Get a response
    session = aiohttp.ClientSession()
    async with session.get(url=api_repo_url) as resp:
        response_json = await resp.text()
        response_body = json.loads(response_json)
    await session.close()

    # Parse a response
    result = dict(
        name=response_body.get('name'),
        avatar=response_body.get('owner', dict()).get('avatar_url'),
        description=response_body.get('description'),
        created_at=response_body.get('created_at'),
        updated_at=response_body.get('updated_at'),
        pushed_at=response_body.get('pushed_at'),
        size=response_body.get('size'),
        subscribers=response_body.get('subscribers_count'),
        forks=response_body.get('forks_count'),
        stars=response_body.get('stargazers_count')
    )
    return result
