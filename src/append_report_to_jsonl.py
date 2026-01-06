import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 17, 
    "prompt": "\"“在当今软件开发行业中，低代码/无代码平台对传统开发流程的影响有多大？它们是否真正提高了开发效率，还是在特定场景下反而增加了维护成本？”\n为什么这个问题有价值？\n行业趋势：低代码/无代码开发近年来发展迅速，许多企业尝试采用它们来加快产品交付速度。 \n生产力 vs. 维护成本：这些工具宣称能降低开发门槛，但长期来看，它们是否真的能提高效率，还是在维护和扩展时带来了更多问题？ \n开发者视角 vs. 业务视角：企业管理者可能认为它们降低了成本，但开发者可能认为它们限制了可扩展性和灵活性。 \n未来发展预测：是否会有越来越多企业完全转向低代码/无代码，还是它们只适用于特定业务场景？\"",
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
