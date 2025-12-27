import json

file_path = "../evaluation_metrics/with_crossover_strategy/full_evals.jsonl"
evaluation_score_path = (
    "../evaluation_metrics/with_crossover_strategy/full_evaluation_score.txt"
)

try:
    overall_score = 0.0
    comprehensiveness_score = 0.0
    insight_score = 0.0
    instruction_following_score = 0.0
    readability_score = 0.0
    item_count = 0
    with open(file_path, "r", encoding="utf-8") as f:
        # Iterate over each line in the file
        for line in f:
            # Parse the JSON string from the current line into a Python dictionary
            try:
                json_object = json.loads(line.strip())
                overall_score += json_object.get("overall_score")
                comprehensiveness_score += json_object.get("comprehensiveness")
                insight_score += json_object.get("insight")
                instruction_following_score += json_object.get("instruction_following")
                readability_score += json_object.get("readability")
                item_count += 1
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line: {line.strip()}. Error: {e}")

    average_score = overall_score / item_count if item_count > 0 else 0.0
    average_comprehensiveness = (
        comprehensiveness_score / item_count if item_count > 0 else 0.0
    )
    average_insight = insight_score / item_count if item_count > 0 else 0.0
    average_instruction_following = (
        instruction_following_score / item_count if item_count > 0 else 0.0
    )
    average_readability = readability_score / item_count if item_count > 0 else 0.0
    print(f"Overall Score of {item_count} items: {average_score}")
    print(f"Comprehensiveness: {average_comprehensiveness}")
    print(f"Insight: {average_insight}")
    print(f"Instruction Following: {average_instruction_following}")
    print(f"Readability: {average_readability}")

    with open(evaluation_score_path, "w") as file:
        file.write(f"Overall Score: {average_score}\n")
        file.write(f"Comprehensiveness: {average_comprehensiveness}\n")
        file.write(f"Insight: {average_insight}\n")
        file.write(f"Instruction Following: {average_instruction_following}\n")
        file.write(f"Readability: {average_readability}\n")
except FileNotFoundError:
    print(f"File not found: {file_path}")
