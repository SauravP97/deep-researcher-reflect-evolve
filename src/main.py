import argparse
from execute_deep_research import execute_deep_research_module
from dotenv import load_dotenv

load_dotenv()
parser = argparse.ArgumentParser(description="Executing Deep Researcher")
parser.add_argument(
    "prompt",
    help="The prompt containing the research task for the Deep Researcher to work on",
)
parser.add_argument(
    "-ecc",
    "--enable_candidate_crossover",
    action="store_true",  # If present, sets to True. If absent, sets to False.
    help="Enable Candidate Crossover algorithm",
)
args = parser.parse_args()
enable_candidate_crossover = args.enable_candidate_crossover
print(f"Starting Deep Research on: {args.prompt}")
print(f"Candidate Crossover enabled = {enable_candidate_crossover}")

execute_deep_research_module(
    args.prompt, enable_candidate_crossover=enable_candidate_crossover
)
