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

research_task = {"id": 37, "topic": "Art & Design", "language": "zh", "prompt": "调研问题：爵士钢琴在现代音乐创作中的创新与风格演变研究 \n背景与问题意识： 爵士钢琴，作为爵士乐的核心组成部分之一，具有独特的演奏技法与即兴创作特性。自20世纪初以来，爵士钢琴从黑色音律的诞生到今各个流派的发展，经历了多次艺术风格的革命与变迁。特别是在现代音乐创作大潮中（尤其是1950年之后），爵士钢琴不仅深受传统爵士乐风格的影响，还不断受到其他音乐流派、比如古典音乐、摇滚乐、电音等风格的冲击和融合。然而，目前对于爵士钢琴在多元化音乐背景下的创新路径与风格演变的系统性研究仍显不足。 随着全球化和音乐的跨界发展，爵士钢琴的演奏和创作不断面临着新的挑战与机会。不同文化背景下的钢琴家在演奏技法、节奏变奏、和声结构等方面的探索，使得爵士钢琴的创作呈现多样性，而这一变化趋势值得深入剖析。\n 本调研旨在探讨爵士钢琴在现代音乐创作中的创新与风格演变。通过对比分析各种创新实践及其对爵士钢琴艺术演变的推动作用，本篇调研将着重分析以下几个方面：一是爵士钢琴从经典爵士到现代爵士的风格演变；二是当代跨流派合作对爵士钢琴的艺术影响；三是技术创新（如音效处理、电子音乐的结合等）和即兴创作手法的革新对爵士钢琴艺术发展的推动。 此项调研将结合数以百计的现代演出视频、音乐创作数据以及关键演奏家访谈，构建一个多层次的分析框架，帮助阐明爵士钢琴在全球音乐创作背景下的持续创新与风格演变，更为理论和创作实践提供深入的分析视角。"}



research_topic = research_task["prompt"]
execute_deep_research_module(
    research_topic,
    enable_candidate_crossover=True,
)
