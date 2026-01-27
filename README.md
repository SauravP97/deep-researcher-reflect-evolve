# Deep Researcher: Sequential Plan Reflection and Candidates Crossover (deepresearch-reflect-evolve)

Deep Researcher is an advanced autonomous agent architecture designed to generate detailed, PhD-level research reports on complex topics. Moving beyond the "parallel scaling" approach of previous agents, this system utilizes `Sequential Research Plan Refinement` and `Candidates Crossover` to achieve superior depth and coherence.

Powered by `gemini-2.5-pro`, Deep Researcher achieves an overall score of `46.21` on the [DeepResearch Bench](https://deepresearch-bench.github.io/), outperforming existing solutions like [Claude Research](https://claude.com/blog/research), [Perplexity Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research), and [Grok Deeper Search](https://x.ai/news/grok-3).

DeepResearch Bench leaderboard: [View](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)


## Running the Deep Researcher

You can execute the Deep Researcher with your research task this way.

```
cd src
python main.py "What are Deep Research Agents"
```

You can also execute the Deep Researcher with the Candidate Crossover algorithm enabled. By default it is disabled.

```
cd src
python main.py "What are Deep Research Agents" -ecc
```


## Key Features

- **Sequential Plan Refinement**: Unlike agents that execute fixed sub-tasks in parallel, this architecture maintains a "Global Research Context" and uses reflection to dynamically update its research plan at runtime based on progress.

- **Candidates Crossover Algorithm**: A search optimization technique where multiple model candidates (with varied `temperature` and `top_k`) investigate queries in parallel. Their findings are synthesized to reduce hallucinations and improve fact density.

- **Global Research Context**: A centralized memory system that stores all search trajectories and artifacts, allowing the agent to reason across the entire research history and avoid "siloed knowledge" problems.

- **One-Shot Report Generation**: Generates the final report in a single pass using the fully matured Global Context, ensuring narrative consistency and high factual density.


## Architecture

The Deep Researcher operates through a cyclic, sequential process that allows for continuous reasoning and course correction.

The 7-Step Workflow

- **Research Plan Curation**: The Planning Agent creates an initial step-by-step plan for the topic.

- **Generate Search Query**: The Search Agent reads the current plan and global context to formulate the next query.

- **Answer Search Query (Candidates Crossover)**: The agent uses the Web Search tool (Tavily) and the Crossover algorithm to gather high-quality information.

- **Research Plan Reflection**: The Planning Agent reviews the Global Context to decide if the plan needs modification.

- **Research Plan Update**: If gaps are found during reflection, the plan is updated dynamically (e.g., adding new sub-topics).

- **Analyze Research Progress**: An LLM-as-a-judge evaluates if the research meets the sufficiency threshold (>90%).

- **One-Shot Report Generation**: Once the loop terminates, the Report Writer synthesizes the final document.


## Candidates Crossover Algorithm

To ensure high-quality data retrieval during Step 3, we implement the Candidates Crossover algorithm, inspired by Google's TTD-DR Self-Evolution [View Paper](https://arxiv.org/pdf/2507.16075).

- **Initialization**: We initialize $n=3$ candidate agents.

- **Diversity**: Each candidate operates with different temperature and top_k configurations to explore varied search spaces.

- **Execution**: Candidates query the web (using Tavily, filtering results with <30% relevance) and generate independent answers.

- **Synthesis**: A crossover mechanism merges these answers into a single, comprehensive response, which is then committed to the Global Context.


## Performance & Evaluation

The model was evaluated using the **DeepResearch Bench**, comprising `100` PhD-level tasks across `22` fields, using the **RACE** (Reference-based Adaptive Criteria-driven Evaluation) framework.

Our Deep Researcher significantly outperforms parallel architectures (like Static-DRA) and major competitors.
DeepResearch Bench leaderboard: [View](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)


| Agent | Overall Score | Comprehensiveness | Insight | Instruction Following | Readability |
|---|---|---|---|---|---|
| Tavily Research | 52.44 | 52.84 | 53.59 | 51.92 | 49.21 |
| Gemini 2.5 Pro DeepResearch | 49.71 | 49.51 | 49.45 | 50.12 | 50.00 |
| Deep Researcher (Ours) | 46.21 | 43.44 | 45.48 | 48.99 | 48.21 |
| Claude Research | 45.00 | 45.34 | 42.79 | 47.58 | 44.66 |
| Perplexity Research | 40.46 | 39.10 | 35.65 | 46.11 | 43.08 |
| Grok Deeper Search | 38.22 | 36.08 | 30.89 | 46.59 | 42.17 |


## Evaluation Strategy

We use [DeepResearch Bench's](https://deepresearch-bench.github.io/) RACE (Reference-based Adaptive Criteria-driven Evaluation) framework to evaluate our Deep Researcher.
We perform a complete evaluation of our Deep Researcher on the entire `100 PhD-level` Research Tasks from `22` distinct fields in `2` languages (English and Chinese).

- [17 Jan 2026] Our Deep Researcher achieved an overall score of `46.21` on the **Deep ResearchBench** making it in the list of **top-10** Deep Researcher worldwide [See Leaderboard](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard) beating `Claude Researcher` and currently `0.24` points below `OpenAI Deep Research`.

- Full Evaluation scores are available here: [View](./evaluation_metrics/with_crossover_strategy/)


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
