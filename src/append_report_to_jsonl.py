import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 15, 
    "prompt": "收集整理目前世界上关于量子网络的研究，横向比较各课题组的相关工作，从以下几个维度，也可以不局限于这些维度：文章发表期刊或会议的等级，课题组成员和领导者的技术背景或学术头衔，课题组经费来源，课题组横向或纵向项目等维度，并为我评估出最有潜力的可以引领未来量子网络发展的十个课题组",
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
