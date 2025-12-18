# Overtool: Slowdown Attacks via Tool Misuse in MCP-Based Reasoning LLMs

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![MCP Protocol](https://img.shields.io/badge/MCP-Protocol-green)](https://github.com/anthropics/mcp)

![Overtool Architecture](./images/architecture.png)

## Overview

Overtool is a framework designed to evaluate the security and performance implications of **OVERTHINK** (slowdown) attacks in reasoning agents using the Model Context Protocol (MCP). While most security research focuses on output correctness, Overtool explores how adversarial prompts can induce agents to expend excessive computation, invoke redundant tools, and process unnecessary context—all while potentially preserving the final output's correctness.

These attacks can result in context window exhaustion, increased latency, and significantly higher computational costs, directly impacting the scalability of MCP-based LLM architectures.

## Attack Methodology

Overtool implements a decoy prompt-based attack strategy using three primary classes of adversarial strategies:

*   **Long Tool Chain Dependency**: Tasks that force the agent into long, sequential tool invocations.
*   **Summarization Decoy**: Injected requests for redundant or excessive summarization at every step.
*   **MDP Decoy (Recursive Reasoning)**: Long recursive reasoning tasks (e.g., Markov Decision Process problems) embedded within natural requests to trigger hidden computation.

## Performance Analysis

We evaluated the impact of these attacks using the **Qwen3-8b** model across various decoy configurations.

### 1. Token Consumption & Execution Runtime
| Task Type | Max Rounds | Avg Prompt Tokens | Avg Output Tokens | Avg Total Tokens | Agent Exec Time (s) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Long Tool Chain Dependency | 10 | 133,008.75 | 8,390.25 | 141,399.00 | 528.20 |
| Long Tool Chain Dependency | 20 | 105,736.43 | 6,352.43 | 112,088.86 | 395.89 |
| Summarization Decoy | 10 | 243,023.00 | 11,824.00 | 254,847.00 | 870.10 |
| Summarization Decoy | 20 | 203,956.00 | 11,592.00 | 215,548.00 | 806.50 |
| MDP Decoy | 10 | 134,529.00 | 11,887.00 | 146,416.00 | 717.00 |
| MDP Decoy | 20 | 101,860.00 | 9,816.00 | 111,676.00 | 595.80 |

### 2. Structural Correctness (Rule-Based)
| Task Type | Max Rounds | Schema Compliance (%) | Valid Tool Name Rate (%) | Tool Call Success Rate (%) |
| :--- | :---: | :---: | :---: | :---: |
| Long Tool Chain Dependency | 10 | 91.19 | 91.67 | 79.59 |
| Long Tool Chain Dependency | 20 | 99.11 | 100.00 | 91.39 |
| Summarization Decoy | 10 | 86.68 | 89.68 | 75.54 |
| Summarization Decoy | 20 | 85.01 | 96.06 | 87.50 |
| MDP Decoy | 10 | 87.14 | 95.66 | 87.17 |
| MDP Decoy | 20 | 88.89 | 92.42 | 86.01 |

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
