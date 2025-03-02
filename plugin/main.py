from pyflowlauncher import Plugin, Result, send_results
from pyflowlauncher.api import open_url, open_setting_dialog
from pyflowlauncher.settings import settings
from pyflowlauncher.icons import RECYCLEBIN, SETTINGS, LINK
from .hoarder import HoarderAPI
from results import query_results, context_menu_results, no_api_token_results, no_base_url_results

plugin = Plugin()

@plugin.on_method
def query(query: str):
    baseUrl = settings().get('hoarderBaseAddress')
    apiKey = settings().get('hoarderApiKey')
    
    if not baseUrl:
        return send_results([no_api_token_results()])
    
    if not apiKey:
        return send_results([no_base_url_results()])
    
    hoarder_api = HoarderAPI(base_url=baseUrl, api_key=apiKey)
    
    return send_results(
        query_results (hoarder_api, query)
    )

@plugin.on_method
def context_menu(data):
    return send_results(context_menu_results(data))

    