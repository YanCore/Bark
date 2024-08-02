from pyflowlauncher.result import ResultResponse, send_results
from pyflowlauncher.jsonrpc import JsonRPCClient
# from BarkNotificator import BarkNotificator
from pyflowlauncher.result import Result
from pyflowlauncher.api import open_url
STARS_PREFIX = "*"
SEPERATOR = "/"

PER_PAGE = 100
SEARCH_LIMIT = 15


def query(query: str) -> ResultResponse:
    settings = JsonRPCClient().recieve().get("settings", {})
    token = settings.get("token", None) or None

    SEPERATOR = ":"
    query = query.strip()
    parsed_query = query.split(SEPERATOR)

    if token:
        # bark = BarkNotificator(device_token=token)
        if len(parsed_query) == 2:
            title, content = parsed_query
            # bark.send(title=title, content=content)
            # bark
            api_url = 'https://api.day.app/{key}/{message}'
            url = api_url.format(key=token, message=f"{title}:{content}")
            result = Result(
                Title=title,
                SubTitle=content,
                JsonRPCAction=open_url(url)
            )
            return send_results(result)
        api_url = 'https://api.day.app/{key}/{message}'
        url = api_url.format(key=token, message=query)
        result = Result(
            Title=query,
            SubTitle=query,
            JsonRPCAction=open_url(url)
        )
        return send_results(result)
