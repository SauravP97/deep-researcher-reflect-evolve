import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 91, 
    "prompt": "I would like a detailed analysis of the Saint Seiya franchise (anime/manga). The analysis should be structured around the different classes of armor (Cloths, Scales, Surplices, God Robes, etc.), such as Bronze Saints, Silver Saints, Gold Saints, Marina Generals, Specters, God Warriors, etc. For each significant character within these categories, provide details on their power level, signature techniques, key appearances/story arcs, and final outcome/fate within the series.",
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
