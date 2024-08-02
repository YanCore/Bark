from pyflowlauncher.result import ResultResponse, send_results
from pyflowlauncher.jsonrpc import JsonRPCClient
from BarkNotificator import BarkNotificator
from pyflowlauncher.result import Result
import requests

STARS_PREFIX = "*"
SEPERATOR = "/"

PER_PAGE = 100
SEARCH_LIMIT = 15


def query(query: str) -> ResultResponse:
    settings = JsonRPCClient().recieve().get("settings", {})
    token = settings.get("token", None) or None
    bark = BarkNotificator(device_token=token)
    SEPERATOR = ":"
    query = query.strip()
    parsed_query = query.split(SEPERATOR)

    if token:
        title, content = parsed_query
        # bark.send(title=title, content=content)
        bark
        api_url = 'https://api.day.app/{key}/{message}'
        url = api_url.format(key=token, message=f"{title}:{content}")
        r = requests.post(url)
        r
        result = Result(
            Title=title,
            SubTitle=content
        )
        return send_results(result)
