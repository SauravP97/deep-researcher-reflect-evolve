import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 9, 
    "prompt": "在计算化学这个领域，我们通常使用Gaussian软件模拟各种情况下分子的结构和性质计算，比如在关键词中加入'field=x+100'代表了在x方向增加了电场。但是，当体系是经典的单原子催化剂时，它属于分子催化剂，在反应环境中分子的朝向是不确定的，那么理论模拟的x方向电场和实际电场是不一致的。请问：通常情况下，理论计算是如何模拟外加电场存在的情况？",
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
