"""Performs Web Searches using Tavily API."""

from langchain_tavily import TavilySearch
from structured_outputs.model_outputs import WebSearchResult


WEB_SEARCH_RELEVANCE_SCORE_THRESHOLD = 0.30


def web_search(query: str) -> list[WebSearchResult]:
    """Perform a web search and return the results"""
    print(f"\n Performing Web Search for {query} \n")

    web_search_tool = TavilySearch(max_results=5)
    web_results = web_search_tool.invoke({"query": query})

    return _parse_web_search_results(web_results)


def _parse_web_search_results(web_search_result) -> list[WebSearchResult]:
    """Parse the web search results and filter based on relevance score"""
    search_results = []

    if not web_search_result or "results" not in web_search_result:
        return search_results

    try:
        for result in web_search_result["results"]:
            print(f"Web Search Result: {result} \n")
            cited_url = result["url"]
            search_content = result["content"]
            search_score = result["score"]

            if search_score >= WEB_SEARCH_RELEVANCE_SCORE_THRESHOLD:
                search_results.append(
                    WebSearchResult(
                        cited_url=cited_url, content=search_content, score=search_score
                    )
                )
    except Exception as e:
        print(f"Error parsing web search results: {e}")
        return []

    return search_results
