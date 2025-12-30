import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 78, 
    "prompt": "Parkinson's disease has a profound impact on patients. What are the potential health warning signs associated with different stages of the disease? As family members, which specific signs should alert us to intervene or seek medical advice regarding the patient's condition? Furthermore, for patients who have undergone Deep Brain Stimulation (DBS) surgery, what daily life adjustments and support strategies can be implemented to improve their comfort and overall well-being?",
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
