from pyflowlauncher import Result
from pyflowlauncher.api import open_url, open_setting_dialog, copy_to_clipboard
from pyflowlauncher.icons import SETTINGS, LINK, ERROR, COPY
from html import unescape

from strip_markdown import strip_markdown
from lib.pyflowlauncher import jsonrpc
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
    """Return a Result from a Hoarder API query item."""
    content = item.get("content")
    match content.get("type"):
        case "link":
            title = content.get("title")
            subtitle = unescape(content.get("description"))
            icon_path = content.get("imageUrl")
            context_data = [{
                "url": content.get("url"),
                "action": "copy_url"
            }]
            json_rpc_action = open_url(content.get("url"))
            return Result(
                Title=title, SubTitle=subtitle, IcoPath=icon_path,
                ContextData=context_data, JsonRPCAction=json_rpc_action
            )
         
        case "text":
            
            title = item.get("title") if item.get("title") else strip_markdown(content.get('text').split('\n')[0])
            title = f"Note: {title}"
            json_rpc_action = copy_to_clipboard(content.get("text"))
            context_data = [{
                "text": content.get("text"),
                "action": "copy_markdown_text"
            }]
            return Result(
                Title=title, CopyText=content.get("text"),
                IcoPath=COPY,
                ContextData=context_data, JsonRPCAction=json_rpc_action
            )

        
def query_results(hoarder: HoarderAPI, query: str):
    search = hoarder.search_bookmarks(query)
    for item in search:
        content = item.get("content")
        if content.get("type") in ("link", "text"):
            yield query_result(item)

def context_menu_results(data):
    for item in data:
        match item.get("action"):
            case "copy_url":
                    yield Result(
                        Title="Copy URL to clipboard",
                        SubTitle="Copy URL to clipboard",
                        IcoPath=LINK,
                        JsonRPCAction=copy_to_clipboard(item.get("url"))
                    )
            case "copy_markdown_text":
                    yield Result(
                        Title="Copy note text to clipboard",
                        SubTitle="Copy note text to clipboard",
                        IcoPath=LINK,
                        JsonRPCAction=copy_to_clipboard(item.get("text"))
                    )                    