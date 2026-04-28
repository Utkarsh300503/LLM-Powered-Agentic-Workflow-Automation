from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

_search = DuckDuckGoSearchRun()

@tool
def search_web(query: str) -> str:
    """Searches the web for recent information on a given query.
    Use this to find current facts, news, or background on any topic."""
    try:
        result = _search.run(query)
        return result
    except Exception as e:
        return f"Search failed: {str(e)}"