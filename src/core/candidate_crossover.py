"""Candidate Cross-Over Strategy for Answering Search Queries"""

from structured_outputs.model_outputs import (
    WebSearchResult,
    SearchAnswer,
)
from language_model.model import Model
from prompts.model_prompts import (
    SEARCH_ANSWER_GENERATION_TEMPLATE,
    SEARCH_ANSWER_CANDIDATES_CROSS_OVER_TEMPLATE,
)

CANDIDATES = 3
CANDIDATES_CONFIGURATION = [
    {
        "top_k": 30,
        "temperature": 0.5,
    },
    {
        "top_k": 40,
        "temperature": 1.0,
    },
    {
        "top_k": 50,
        "temperature": 1.5,
    },
]


def answer_search_query_with_candidate_crossover(
    research_topic: str, search_query: str, web_search_response: list[WebSearchResult]
) -> SearchAnswer:
    """Answer the search query using candidate cross-over strategy"""
    print("Answering search query with candidate cross-over strategy...")
    candidate_answers: list[str] = []
    for config in CANDIDATES_CONFIGURATION:
        model = Model(temperature=config["temperature"], top_k=config["top_k"])
        response = model.call_model_with_structured_output(
            SEARCH_ANSWER_GENERATION_TEMPLATE.format(
                research_topic=research_topic,
                current_query=search_query,
                search_results="\n".join(
                    f"{web_search_result['content']} ({web_search_result['cited_url']})"
                    for web_search_result in web_search_response
                ),
            ),
            SearchAnswer,
        )
        candidate_answers.append(response["answer"])
    answer_after_crossover: str = candidates_cross_over(
        research_topic, candidate_answers
    )

    return {
        "answer": answer_after_crossover,
        "citations": [],
    }


def candidates_cross_over(research_topic: str, candidate_answers: list[str]) -> str:
    """Combine multiple candidate answers into a single improved answer"""
    print("Performing candidates cross-over...")
    model = Model()
    response = model.call_model(
        SEARCH_ANSWER_CANDIDATES_CROSS_OVER_TEMPLATE.format(
            query=research_topic,
            answer_list="\n\n".join(
                f"Answer of Candidate {i+1}:\n{answer} \n\n"
                for i, answer in enumerate(candidate_answers)
            ),
        )
    )

    return response.content
