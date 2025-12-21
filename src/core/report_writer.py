from prompts.model_prompts import REPORT_WRITER_TEMPLATE
from language_model.model import Model


def write_detailed_report(
    research_topic: str, research_plan: str, aggregated_research_logs: str
) -> str:
    """Generate a detailed research report based on the provided inputs."""
    model = Model()
    report = model.call_model(
        REPORT_WRITER_TEMPLATE.format(
            research_topic=research_topic,
            research_plan=research_plan,
            aggregated_research_logs=aggregated_research_logs,
        )
    )

    return report.content
