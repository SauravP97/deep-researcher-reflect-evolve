"""Search agent module for Query generation and Answer retrieval."""

from structured_outputs.model_outputs import (
    ResearchPlan,
    SearchQuery,
    WebSearchResult,
    SearchAnswer,
)
from prompts.model_prompts import (
    SEARCH_QUERY_GENERATION_TEMPLATE,
    SEARCH_ANSWER_GENERATION_TEMPLATE,
)
from language_model.model import Model
from core.web_search import web_search


def generate_search_query(research_topic, research_plan: ResearchPlan) -> SearchQuery:
    """Generate a search query based on the research topic, plan and past context"""
    model = Model()
    response = model.call_model_with_structured_output(
        SEARCH_QUERY_GENERATION_TEMPLATE.format(
            research_topic=research_topic,
            research_plan="\n".join([step for step in research_plan["steps"]]),
            search_history="[]",
        ),
        SearchQuery,
    )

    return response


def answer_search_query(research_topic: str, query: str) -> SearchAnswer:
    """Answer the search query using web search results"""
    model = Model()
    web_search_response: list[WebSearchResult] = web_search(query)
    response = model.call_model_with_structured_output(
        SEARCH_ANSWER_GENERATION_TEMPLATE.format(
            research_topic=research_topic,
            current_query=query,
            search_results="\n".join(
                f"{web_search_result['content']} ({web_search_result['cited_url']})"
                for web_search_result in web_search_response
            ),
        ),
        SearchAnswer,
    )

    return response
