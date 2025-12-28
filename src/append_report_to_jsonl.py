import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 54, 
    "prompt": "In the field of FinTech, machine learning algorithms are now widely applied to asset allocation and investment decisions. Examples include classic models like Mean-Variance and Black-Litterman, as well as emerging deep learning models. While these models have shown certain advantages under different market conditions, each also has its limitations. For instance, the Mean-Variance model assumes asset returns follow a normal distribution, which often doesn't align with actual market conditions. The Black-Litterman model relies on subjective view inputs, introducing a degree of subjectivity. Although deep learning models can handle complex non-linear relationships, they suffer from poor interpretability. So, what are the core differences between these various models in terms of risk measurement, return prediction, and asset allocation? And is it possible to combine their strengths to build a more general-purpose and effective modeling framework?",
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
