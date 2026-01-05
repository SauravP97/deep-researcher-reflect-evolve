import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 12, 
    "prompt": "收集整理近10年来国际上自来水生产及销售企业在技术创新且已经实现创新成果产业化应用方面，按技术产业化应用实现的经济收益规模前10的创新成果，列举企业名称，技术创新成果及产业化应用情况，对比分析国内同类型水务企业的情况，给出国内水务企业以实现技术创新成果产业化应用为目的可重点开展技术攻关的3-5个方向的建议",
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
