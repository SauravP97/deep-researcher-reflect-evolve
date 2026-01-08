import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 22, 
    "prompt": "中国的艺术生就业领域长期以来较为单一，主要集中在传统艺术机构、教育部门或文创企业。随着社会的发展，艺术与科技、商业、教育等领域的边界正在模糊，为艺术生提供了更广阔的职业发展空间。然请为我调研：艺术生如何突破传统就业领域的限制，实现多元化职业发展？当前社会评价体系如何影响艺术人才的发展空间与收入水平？知识产权保护与文化消费升级能否有效提升艺术人才经济待遇？不同国家在艺术人才社会地位提升方面有哪些可借鉴的经验与模式？",
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
