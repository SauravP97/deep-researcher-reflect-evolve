import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 80, 
    "prompt": "Please investigate the influence of mass media on language, specifically the queer community of Japan. I am trying to see if the consumption of shoujo manga by queer Japanese young adults affects their pronoun use and sentence ending particles. Both grammatical categories are gendered in Japanese and a distinct pattern emerges in shoujo manga compared to majority use in society, so observing a minority group would give insight into the effect of media in personal expression.",
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
