import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 14, 
    "prompt": "收集整理全球数学与量子计算交叉领域的主要研究团队及其成果，横向比较其研究方向、论文产出、国际合作、资金支持、工业界合作等维度，评估哪些团队最有可能在未来5-10年内推动量子计算技术的重大突破，并预测可能产生的关键性数学理论或应用技术",
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
