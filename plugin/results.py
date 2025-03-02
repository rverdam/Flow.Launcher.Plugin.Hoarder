from pyflowlauncher import Result
from pyflowlauncher.api import open_url, open_setting_dialog, copy_to_clipboard
from pyflowlauncher.icons import RECYCLEBIN, SETTINGS, LINK, ERROR
from html import unescape

from plugin.hoarder import HoarderAPI

def error_results(error: str, JsonRPCAction=None):
    return Result(
        Title="Hoarder Plugin Error",
        SubTitle=error,
        IcoPath=ERROR,
        JsonRPCAction=JsonRPCAction
    )

def no_base_url_results():
    return Result(
        Title="No Hoarder Base Address found!",
        SubTitle="Please enter your Hoarder Base Address in plugin settings.",
        IcoPath=SETTINGS,
        JsonRPCAction=open_setting_dialog()
    )
    

def no_api_token_results():
    return Result(
        Title="No API key found!",
        SubTitle="Please enter your Hoarder API key in plugin settings.",
        IcoPath=SETTINGS,
        JsonRPCAction=open_setting_dialog()
    )


def query_result(item) -> Result:
    return Result(
        Title=item["content"]["title"],
        SubTitle=unescape(item["content"]["description"]),
        IcoPath=item["content"]["imageUrl"],
        ContextData=[item["content"]["url"]],
        JsonRPCAction=open_url(item["content"]["url"]),
    )


def query_results(hoarder: HoarderAPI, query: str):
    search = hoarder.search_bookmarks(query)
    for item in search:
        yield query_result(item)

def context_menu_results(data):
    
    yield Result(
        Title="Copy URL to clipboard",
        SubTitle="Copy URL to clipboard",
        IcoPath=LINK,
        JsonRPCAction=copy_to_clipboard(data[0])
    )