import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 10,
    "prompt": "在800V高压/碳化硅电驱/固态电池/分布式驱动等技术迭代加速的窗口期，如何构建覆盖研发制造-使用场景-残值管理的评估体系，量化不同动力系统技术路线（纯电/增程/插混/氢燃料+集中式驱动/分布式驱动）的商业化临界点？",
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
