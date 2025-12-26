import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
   "id": 76, 
   "prompt": "The significance of the gut microbiota in maintaining normal intestinal function has emerged as a prominent focus in contemporary research, revealing both beneficial and detrimental impacts on the equilibrium of gut health. Disruption of microbial homeostasis can precipitate intestinal inflammation and has been implicated in the pathogenesis of colorectal cancer. Conversely, probiotics have demonstrated the capacity to mitigate inflammation and retard the progression of colorectal cancer. Within this domain, key questions arise: What are the predominant types of gut probiotics? What precisely constitutes prebiotics and their mechanistic role? Which pathogenic bacteria warrant concern, and what toxic metabolites do they produce? How might these findings inform and optimize our daily dietary choices?",
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
