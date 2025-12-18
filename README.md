# Overtool: Slowdown Attacks via Tool Misuse in MCP-Based Reasoning LLMs

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![MCP Protocol](https://img.shields.io/badge/MCP-Protocol-green)](https://github.com/anthropics/mcp)

![Overtool Architecture](./images/architecture.png)

## Overview

Overtool is a framework designed to evaluate the security and performance implications of **slowdown attacks** in tool-augmented reasoning agents built using the Model Context Protocol (MCP). Unlike prior work that primarily focuses on output correctness or malicious tool behavior, Overtool studies how adversarial prompts can induce agents to expend excessive computation, invoke redundant tools, and process unnecessary context.

These slowdown attacks significantly increase execution latency and computational cost and, in stronger cases, can degrade planning quality or cause task non-completion. Our results demonstrate that in MCP-based systems, such attacks can cascade across multiple planning rounds and tool invocations, amplifying performance overhead in multi-server agent executions.

## Threat Model

We consider an adversary that can influence user-facing prompts provided to MCP-based reasoning agents. The adversary’s objective is to induce excessive reasoning and redundant tool usage by injecting decoy tasks that stress long-horizon planning and multi-tool execution.

The attack does **not** require compromising MCP servers or modifying tool metadata. Instead, it exploits inefficiencies in agent planning and execution behavior, leading to increased latency, higher computational cost, and in stronger cases, task failure or denial of task completion.

## Attack Methodology

Overtool implements **prompt-level slowdown attacks** using structured decoy injection designed to stress multi-round planning and tool orchestration in MCP-based reasoning agents. We evaluate three primary classes of adversarial strategies:

- **Long Tool Chain Dependency**  
  Tasks that force the agent into long, sequential tool invocations across multiple MCP servers.

- **Summarization Decoy**  
  Injected requests for redundant or excessive summarization at intermediate steps, increasing token usage and execution time.

- **MDP Decoy (Recursive Reasoning)**  
  Long recursive reasoning tasks (e.g., Markov Decision Process problems) embedded within natural requests to trigger excessive internal computation and planning overhead.

## Evaluation Pipeline

Overtool evaluates agent behavior using a three-stage evaluation pipeline:

- **LLM-as-a-Judge**  
  Evaluates planning quality, tool appropriateness, and overall task fulfillment.

- **Rule-Based Engine**  
  Measures structural correctness, schema compliance, and tool invocation validity.

- **Execution Statistics**  
  Tracks wall-clock runtime, agent execution time, number of tool calls, and token usage.

This pipeline enables analysis of both qualitative reasoning degradation and quantitative system-level performance impact induced by slowdown attacks.

## Performance Analysis

We evaluated the impact of these attacks using the **Qwen3-8B** reasoning model across multiple adversarial decoy configurations. Experiments were conducted using realistic multi-tool MCP tasks spanning up to 28 MCP servers.

### Token Consumption & Execution Runtime

| Task Type | Max Rounds | Avg Prompt Tokens | Avg Output Tokens | Avg Total Tokens | Agent Exec Time (s) |
|----------|------------|-------------------|-------------------|------------------|--------------------|
| Long Tool Chain Dependency | 10 | 133,008.75 | 8,390.25 | 141,399.00 | 528.20 |
| Long Tool Chain Dependency | 20 | 105,736.43 | 6,352.43 | 112,088.86 | 395.89 |
| Summarization Decoy | 10 | 243,023.00 | 11,824.00 | 254,847.00 | 870.10 |
| Summarization Decoy | 20 | 203,956.00 | 11,592.00 | 215,548.00 | 806.50 |
| MDP Decoy | 10 | 134,529.00 | 11,887.00 | 146,416.00 | 717.00 |
| MDP Decoy | 20 | 101,860.00 | 9,816.00 | 111,676.00 | 595.80 |

### Structural Correctness (Rule-Based Metrics)

| Task Type | Max Rounds | Schema Compliance (%) | Valid Tool Name Rate (%) | Tool Call Success Rate (%) |
|----------|------------|------------------------|--------------------------|----------------------------|
| Long Tool Chain Dependency | 10 | 91.19 | 91.67 | 79.59 |
| Long Tool Chain Dependency | 20 | 99.11 | 100.00 | 91.39 |
| Summarization Decoy | 10 | 86.68 | 89.68 | 75.54 |
| Summarization Decoy | 20 | 85.01 | 96.06 | 87.50 |
| MDP Decoy | 10 | 87.14 | 95.66 | 87.17 |
| MDP Decoy | 20 | 88.89 | 92.42 | 86.01 |

### Token Usage Graphs

#### Prompt Token Usage
![Prompt Token Usage](figures/Figure1.png)

#### Output Token Usage
![Output Token Usage](figures/figure2.png)

## Quick Start

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/[your-username]/mcp-attacks-overtool.git
cd mcp-attacks-overtool
```

2. **Install dependencies**
```bash
conda create -n overtool python=3.10
conda activate overtool
cd mcp_servers
bash ./install.sh
cd ..
```

3. **Set up environment variables**
```bash
cat > .env << EOF
export OPENROUTER_API_KEY="your_openrouterkey_here"
export AZURE_OPENAI_API_KEY="your_azureopenai_apikey_here"
export AZURE_OPENAI_ENDPOINT="your_azureopenai_endpoint_here"
EOF
```

### Running Overtool Attacks

To run the benchmark with decoy prompt injection:

```bash
# 1. Verify connections
python ./utils/collect_mcp_info.py

# 2. Run benchmark with attack tasks
source .env
python run_benchmark.py --models qwen3-8b --tasks-file tasks/injected_prompt_template.md
```

## MCP Servers

Overtool leverages 28 diverse MCP servers for realistic task execution:

- [BioMCP](https://github.com/genomoncology/biomcp) - Biomedical research data
- [Wikipedia](https://github.com/Rudra-ravi/wikipedia-mcp) - Encyclopedia content
- [Reddit](https://github.com/dumyCq/mcp-reddit) - Social media discussions
- [Unit Converter](https://github.com/zazencodes/unit-converter-mcp) - Measurement conversions
- [NASA Data](https://github.com/AnCode666/nasa-mcp) - Space mission data
- ... and 23 others.

## Project Structure

```
mcp-attacks-overtool/
├── agent/                     # Task execution agents
├── benchmark/                 # Evaluation framework
├── synthesis/                # Task generation & Decoy Injection
│   ├── task_synthesis.py     # Core attack logic
│   └── injected_prompt_template.md # Attack templates
├── tasks/                    # Benchmark task files
├── mcp_servers/             # 28 integrated MCP servers
└── run_benchmark.py         # Main orchestrator
```

## Citation

If you use Overtool in your research, please cite:

```bibtex
@article{khan2025overtool,
  title={Overtool: Slowdown Attacks via Tool Misuse in MCP-Based Reasoning LLMs},
  author={Khan, Zaifa and Madadi, Chetan and Mohanraj, Sanjiv Kumaran},
  year={2025}
}
```

## Acknowledgments

- Built on the [Model Context Protocol](https://github.com/anthropics/mcp) by Anthropic
- Inspired by the [MCP-Bench](https://github.com/accenture/mcp-bench) evaluation framework
- Special thanks to the UMass Amherst CS685 - Advanced NLP course staff.
