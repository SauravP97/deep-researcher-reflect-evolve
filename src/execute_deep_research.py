from dotenv import load_dotenv
from core.planning_agent import plan_for_research_topic
from core.search_agent import generate_search_query
from structured_outputs.model_outputs import ResearchPlan

print("Executing Deep Research Module...")
load_dotenv()
research_plan = plan_for_research_topic("AI in Healthcare")
search_query = generate_search_query("AI in Healthcare", research_plan)
