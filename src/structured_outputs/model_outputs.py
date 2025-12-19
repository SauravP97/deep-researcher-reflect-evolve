from pydantic import BaseModel


class ResearchPlan(BaseModel):
    """Schema for research plan output."""
    steps: list[str]
