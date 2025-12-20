from dotenv import load_dotenv
from core.planning_agent import plan_for_research_topic
from core.search_agent import generate_search_query, answer_search_query
from structured_outputs.model_outputs import ResearchPlan

print("Executing Deep Research Module...")
load_dotenv()
research_topic = "AI in Healthcare"
research_plan = plan_for_research_topic(research_topic)
print("Generated Research Plan:")
print("\n".join([f"Step: {step}" for step in research_plan["steps"]]))
print("\n\n")

search_query = generate_search_query(research_topic, research_plan)
print("Generated Search Query: ", search_query["query"])
print("\n\n")

search_answer = answer_search_query(research_topic, search_query["query"])
print("Generated Search Answer: ", search_answer["answer"])
