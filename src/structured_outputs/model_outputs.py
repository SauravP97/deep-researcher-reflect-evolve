from pydantic import BaseModel
from typing_extensions import TypedDict


class ResearchPlan(BaseModel):
    """Schema for research plan output."""

    steps: list[str]


class SearchQuery(BaseModel):
    """Schema for search query output."""

    query: str


class WebSearchResult(TypedDict):
    """Schema for web search result output."""

    cited_url: str
    content: str
    score: float


class SearchAnswer(BaseModel):
    """Schema for search answer output."""

    answer: str
    citations: list[str]


class ResearchPlanReflection(BaseModel):
    """Schema for research plan reflection output."""

    should_update: bool
    updates: str


class ResearchProgress(BaseModel):
    """Schema for research progress output."""

    progress: int
