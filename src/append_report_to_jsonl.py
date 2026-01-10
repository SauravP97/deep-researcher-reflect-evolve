import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 29, 
    "prompt": "50年代至今，中国大陆中国古代文学研究头部学者知识背景差异调查\n具体做法：收集整理50年代至今从事中国古代文学学科研究的头部学者的毕业院校、院校学科总体偏向，及专业、学历、工作经历、导师的专业背景等，和不同时期的文艺方针、学术潮流等时代背景，加权计算，分析比较得出某个特定时期的学者学科背景同异，以及个人的知识构成。",
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
