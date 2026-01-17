# Deep Researcher with Candidates Crossover and Plan Reflection

Building...

## Evaluation Strategy

We use [DeepResearch Bench's](https://deepresearch-bench.github.io/) RACE (Reference-based Adaptive Criteria-driven Evaluation) framework to evaluate our Deep Researcher.

1. We perform a complete evaluation of our Deep Researcher on the entire `100 PhD-level` Research Tasks from `22` distinct fields in `2` languages (English and Chinese).

    - [17 Jan 2026] Our Deep Researcher achieved an overall score of `46.21` on the **Deep ResearchBench** making it in the list of **top-10** Deep Researcher worldwide [See Leaderboard](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard) beating `Claude Researcher` and currently `0.24` points below `OpenAI Deep Research`.

    - Full Evaluation scores are available here: [View](./evaluation_metrics/with_crossover_strategy/) 

2. With vs Without Candidate Cross Over: We evaluate our Deep Researcher on `3 PhD-level` Research Tasks from 5 distinct fields. The first evaluation exercise is performed without involving the Crossover strategy and the second exercise involving that strategy.

    - Distinct Fields:
        - Education and Jobs
        - Finance and Business
        - Health
        - Science and Technology
        - Software Development


## Cost for Research Report generation and Evaluation on the benchmark

**Overall Evaluation Cost**: `USD 401.25` (`INR 36,222.78`)

1. Dec 2025: `USD 157.60` (`INR 14,186.28`)
2. Jan 2026: `USD 243.65` (`INR 21,994.78`)

> Note: USD to INR exchange rates as of period around Dec & Jan 2026

## Execution and Pre-requisites

### Execution Steps

1. Place your API Key in the `.env` file within the `/src` directory.
2. Run the following command 
```
cd src
python execute_deep_research.py
```

### External Libraries and Virtual Environment

Prefer using virtual environment for managing external library dependencies.

- You can setup your virtual environment with the following command
```
pip install virtualenv
virtualenv <your_environment_name>
```
- Activate your virtual environment:
```
source <your_environment_name>/bin/activate
```
- Deactivate your virtual environment:
```
deactivate
```

### Install external Libraries (Required)

```
pip install virtualenv
pip install dotenv
pip install langchain-google-genai
pip install langchain-tavily
```
