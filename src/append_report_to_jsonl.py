import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 83, 
    "prompt": "Acting as a senior hardware product manager, conduct in-depth research on tablet-style devices used for payments or SaaS applications. Your report should: 1) List major manufacturers, specific device models, and their configurations. 2) Include images of these devices. 3) Analyze the primary use cases and scenarios where these devices are deployed. 4) Investigate the market penetration, common usage scenarios, typical price ranges, and estimated installed base for such devices across different regions (North America, Japan/Korea, Southeast Asia, South America).",
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
