from dotenv import load_dotenv
from core.planning_agent import (
    plan_for_research_topic,
    reflect_on_research_plan,
    maybe_update_research_plan,
    analyze_research_progress,
)
from core.search_agent import generate_search_query, answer_search_query
from structured_outputs.model_outputs import ResearchPlan, ResearchPlanReflection
from agent_context.context_utils import (
    add_past_chat_to_context,
    get_full_context,
    clear_context,
)
from core.report_writer import write_detailed_report


MAX_CYCLES = 30
PERCENTAGE_THRESHOLD = 90.0
AGENT_CONTEXT_PATH = "agent_context/context.txt"
REPORT_PATH = "generated_report/report.md"


def execute_deep_research_module(
    research_topic: str, enable_candidate_crossover: bool = False
):
    """Executes the Deep Research Module for a given research topic."""
    print("Executing Deep Research Module...")
    research_plan = plan_for_research_topic(research_topic)
    print("Generated Research Plan:")
    print("\n".join([f"Step: {step}" for step in research_plan["steps"]]))
    print("\n\n")
    clear_context(AGENT_CONTEXT_PATH)

    citations = []
    steps = 0
    while steps < MAX_CYCLES:
        print(f"--- Research Loop: {steps} --- \n")
        search_query = generate_search_query(
            research_topic, research_plan, get_full_context(AGENT_CONTEXT_PATH)
        )
        print("Generated Search Query: ", search_query["query"])
        print("\n\n")

        search_answer = answer_search_query(
            research_topic, search_query["query"], enable_candidate_crossover
        )
        citations.extend(search_answer["citations"])
        print("Generated Search Answer: ", search_answer["answer"])
        print("\n\n")

        add_past_chat_to_context(search_query, search_answer, AGENT_CONTEXT_PATH)

        research_plan_reflection: ResearchPlanReflection = reflect_on_research_plan(
            research_topic, research_plan, get_full_context(AGENT_CONTEXT_PATH)
        )
        research_plan = maybe_update_research_plan(
            research_topic, research_plan, research_plan_reflection
        )
        steps += 1

        progress = 0.0
        if steps % 5 == 0:
            progress = analyze_research_progress(
                research_topic, research_plan, get_full_context(AGENT_CONTEXT_PATH)
            )
            print(f"Interim Research Progress after {steps} steps: {progress}%\n\n")

        if progress > PERCENTAGE_THRESHOLD:
            print("Research progress satisfactory, ending research loop.\n\n")
            break

    progress = analyze_research_progress(
        research_topic, research_plan, get_full_context(AGENT_CONTEXT_PATH)
    )
    print(f"Final Research Progress: {progress}%\n\n")

    return write_deep_research_report(research_topic, research_plan, citations)


def write_deep_research_report(
    research_topic: str, research_plan: ResearchPlan, citations: list[str]
) -> str:
    """Writes a detailed research report based on the completed research."""
    print("Writing Detailed Research Report...")
    aggregated_research_logs = get_full_context(AGENT_CONTEXT_PATH)
    report = write_detailed_report(
        research_topic, "\n".join(research_plan["steps"]), aggregated_research_logs
    )

    with open(REPORT_PATH, "w") as file:
        file.write(f"# {research_topic}\n\n")
        file.write(report)
        file.write("\n\n")
        file.write("## Citations \n")
        file.write("\n".join([f"- {citation}" for citation in citations]))

    return report


load_dotenv()

research_task = {"id": 22, "topic": "Education & Jobs", "language": "zh", "prompt": "中国的艺术生就业领域长期以来较为单一，主要集中在传统艺术机构、教育部门或文创企业。随着社会的发展，艺术与科技、商业、教育等领域的边界正在模糊，为艺术生提供了更广阔的职业发展空间。然请为我调研：艺术生如何突破传统就业领域的限制，实现多元化职业发展？当前社会评价体系如何影响艺术人才的发展空间与收入水平？知识产权保护与文化消费升级能否有效提升艺术人才经济待遇？不同国家在艺术人才社会地位提升方面有哪些可借鉴的经验与模式？"}



research_topic = research_task["prompt"]
execute_deep_research_module(
    research_topic,
    enable_candidate_crossover=True,
)
