import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 18, 
    "prompt": "请你学习一下GCS算法的原理。目前的GCS算法主要是用于安全凸集内的路径自动求解。目前，针对凸集的生成，采用的是人工手动播种结合自动化工具的方式，在离线时生成安全区域凸集。现在我想探寻一种自动化生成安全区域的方式，来进一步优化这个GCS算法。例如，能否结合PRM算法（或改进的PRM算法），生成一个静态联通图，再结合凸算法，自动构造一个凸集，把凸集直接供给GCS算法求解。能不能帮我详细分析这个优化思路是否可行？要如何展开？或者能否提供其他的基于GSC算法的优化思路？",
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
