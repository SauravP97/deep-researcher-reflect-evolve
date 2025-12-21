"""Planning agent module."""

from prompts.model_prompts import (
    RESEARCH_PLANNING_TEMPLATE,
    RESEARCH_PLAN_REFLECTION_TEMPLATE,
    RESEARCH_PLAN_UPDATE_TEMPLATE,
    RESEARCH_PROGRESS_TEMPLATE,
)
from language_model.model import Model
from structured_outputs.model_outputs import (
    ResearchPlan,
    ResearchPlanReflection,
    ResearchProgress,
)


def plan_for_research_topic(research_topic: str) -> ResearchPlan:
    """Generate a research plan for the given topic."""
    model = Model()
    response: ResearchPlan = model.call_model_with_structured_output(
        RESEARCH_PLANNING_TEMPLATE.format(research_topic=research_topic), ResearchPlan
    )

    return response


def reflect_on_research_plan(
    research_topic: str, research_plan: ResearchPlan, search_history: str
) -> ResearchPlanReflection:
    """Reflect on the research plan given past context and decide whether to update it."""
    model = Model()
    response: ResearchPlanReflection = model.call_model_with_structured_output(
        RESEARCH_PLAN_REFLECTION_TEMPLATE.format(
            research_topic=research_topic,
            research_plan="\n".join([step for step in research_plan["steps"]]),
            search_history=search_history,
        ),
        ResearchPlanReflection,
    )

    return response


def maybe_update_research_plan(
    research_topic: str,
    research_plan: ResearchPlan,
    research_plan_reflection: ResearchPlanReflection,
) -> ResearchPlan:
    """Update the research plan based on reflection."""
    if research_plan_reflection["should_update"]:
        print("Updating research plan based on reflection...")
        model = Model()
        updated_research_plan: ResearchPlan = model.call_model_with_structured_output(
            RESEARCH_PLAN_UPDATE_TEMPLATE.format(
                research_topic=research_topic,
                research_plan="\n".join([step for step in research_plan["steps"]]),
                updates=research_plan_reflection["updates"],
            ),
            ResearchPlan,
        )
        return updated_research_plan
    else:
        print("No updates to research plan needed.")
        return research_plan


def analyze_research_progress(
    research_topic: str, research_plan: ResearchPlan, search_history: str
) -> int:
    """Analyze research progress."""
    model = Model()
    research_progress: ResearchProgress = model.call_model_with_structured_output(
        RESEARCH_PROGRESS_TEMPLATE.format(
            research_topic=research_topic,
            research_plan="\n".join([step for step in research_plan["steps"]]),
            search_history=search_history,
        ),
        ResearchProgress,
    )

    return research_progress["progress"]
