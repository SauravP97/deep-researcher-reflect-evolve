from dotenv import load_dotenv
from core.planning_agent import plan_for_research_topic

print("Executing Deep Research Module...")
load_dotenv()
plan_for_research_topic("AI in Healthcare")