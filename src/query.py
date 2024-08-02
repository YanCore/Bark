from pyflowlauncher.result import ResultResponse, send_results
from pyflowlauncher.jsonrpc import JsonRPCClient
from BarkNotificator import BarkNotificator
from pyflowlauncher.result import Result

STARS_PREFIX = "*"
SEPERATOR = "/"

PER_PAGE = 100
SEARCH_LIMIT = 15


def query(query: str) -> ResultResponse:
    settings = JsonRPCClient().recieve().get("settings", {})
    token = settings.get("token", None) or None
    bark = bark = BarkNotificator(device_token=token)
    SEPERATOR = ":"
    query = query.strip()
    parsed_query = query.split(SEPERATOR)

    if token:
        title, content = parsed_query
        bark.send(title=title, content=content)

        result = Result(
            Title=repo.full_name,
            SubTitle=repo.description,
            IcoPath=repo.owner.avatar_url,
            JsonRPCAction=open_url(repo.html_url),
            CopyText=repo.full_name,
            ContextData=[repo.full_name, repo.html_url],
        )
        return send_results(result)
