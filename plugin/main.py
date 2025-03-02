from pyflowlauncher import Plugin, Result, send_results
from pyflowlauncher.api import open_url
from pyflowlauncher.result import ResultResponse
from pyflowlauncher.settings import settings
from .hoarder import HoarderAPI
from html import unescape

plugin = Plugin()

@plugin.on_method
def query(query: str) -> ResultResponse:
    baseUrl = settings().get('hoarderBaseAddress')
    apiKey = settings().get('hoarderApiKey')
    hoarder_api = HoarderAPI(base_url=baseUrl, api_key=apiKey)

    results = hoarder_api.search_bookmarks(query)

    return send_results([Result(
        Title=result['content']['title'],
        SubTitle=unescape(result['content']['description']),
        IcoPath=result['content']['imageUrl'],
        JsonRPCAction=open_url(result['content']['url'])
    ) for result in results])



    