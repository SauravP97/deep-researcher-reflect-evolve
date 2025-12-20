"""Search agent module for Query generation and Answer retrieval."""

from structured_outputs.model_outputs import ResearchPlan, SearchQuery
from prompts.model_prompts import SEARCH_QUERY_GENERATION_TEMPLATE
from language_model.model import Model


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
    print("Generated Search Query:", response["query"])

    return response
