import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 27, 
    "prompt": "如何将AI心理咨询和人类心理咨询有机结合，以便为人类心理健康谋求福利？",
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
    json.dump(existing_data, file, indent=4, ensure_ascii=False)
