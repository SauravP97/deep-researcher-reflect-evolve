import json

report_content = ""
try:
    with open("./generated_report/report.md", "r") as file:
        report_content = file.read()
except FileNotFoundError:
    report_content = ""  # Initialize as an empty string if the file doesn't exist

report_object = {
    "id": 68, 
    "prompt": "I need to dynamically adjust Kubernetes (K8S) cluster node counts based on fluctuating business request volumes, ensuring resources are scaled up proactively before peak loads and scaled down promptly during troughs. The standard Cluster Autoscaler (CA) isn't suitable as it relies on pending pods and might not fit non-elastic node group scenarios. What are effective implementation strategies, best practices, or existing projects that address predictive or scheduled autoscaling for K8S nodes?",
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
    json.dump(existing_data, file, indent=4)
