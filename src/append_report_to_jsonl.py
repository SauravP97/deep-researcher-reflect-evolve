import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 26, 
    "prompt": "为我调研在慢性抗原刺激下（如肿瘤微环境或HIV潜伏感染），CD8+ T细胞线粒体动力学（融合/裂变平衡）如何通过调控表观遗传重塑（如m6A修饰、乳酸介导的组蛋白乳酸化）驱动终末耗竭与组织驻留记忆（Trm）细胞命运分岔，基于代谢-表观遗传互作网络定量建模",
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
