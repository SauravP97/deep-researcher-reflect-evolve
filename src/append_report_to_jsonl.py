import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 25, 
    "prompt": "请为我整合近几年有关“中性粒细胞在脑缺血急性期和慢性期的功能和发展变化”的研究成果。在此基础上预测中性粒细胞各个亚群如何和其他的细胞类型发生相互作用，最终如何导向不同的临床结局。最后，为我分析未来可能需要开展的工作。",
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
