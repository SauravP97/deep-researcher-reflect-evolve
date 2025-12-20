"""Planning agent module."""

from prompts.model_prompts import RESEARCH_PLANNING_TEMPLATE
from language_model.model import Model
from structured_outputs.model_outputs import ResearchPlan


def plan_for_research_topic(research_topic) -> ResearchPlan:
    """Generate a research plan for the given topic."""
    model = Model()
    response: ResearchPlan = model.call_model_with_structured_output(
        RESEARCH_PLANNING_TEMPLATE.format(research_topic=research_topic), ResearchPlan
    )

    return response
