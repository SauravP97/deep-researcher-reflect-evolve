import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
   "id": 95, 
   "prompt": "Create comprehensive, in-depth study notes for the Diamond Sutra (Vajracchedikā Prajñāpāramitā Sūtra). These notes should offer deep analysis and interpretation from various perspectives, exploring its teachings and relevance in contexts such as daily life, the workplace/career, business practices, marriage, parenting, emotional well-being, and interpersonal dynamics.",
    "article": report_content,
}

filename = "./generated_report/model_output.jsonl"

try:
    with open(filename, "r") as file:
        existing_data = json.load(file)
except FileNotFoundError:
    existing_data = []  # Initialize as an empty list if the file doesn't exist

# Example for appending to a list within a dictionary
if isinstance(existing_data, list):
    existing_data.append(report_object)

with open(filename, "w") as file:
    json.dump(existing_data, file, indent=4)
