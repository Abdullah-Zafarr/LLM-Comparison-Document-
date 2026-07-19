# AI Engineering Lab: LLM Summarization Benchmarking & Tokenization Study

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
</p>

Welcome to the **LLM Benchmarking & Tokenization Analysis** workspace! This laboratory repository evaluates and compares structural accuracy, tokenization efficiency, and deployment economics of Large Language Models (LLMs) on document summarization, comparing traditional **Retrieval-Augmented Generation (RAG)** systems against native **Long-Context Window** models.

We analyze five modern cognitive architectures: **GPT 5.5 Instant**, **Claude 4.7 Sonnet**, **Gemini 3.1 Pro**, **DeepSeek-R1**, and **Llama 3.3 (70B)**.

---

## Unique Model Evaluation Benchmarks

To avoid generic rating layouts, our benchmark grades each candidate across blended qualitative metrics, tracking syntactic layout, semantic integrity, and core advantages:

### 🏆 Custom Performance & Quality Ledger

| LLM Benchmark Candidate | Structure & Formatting <br>*(Quality & Conciseness)* | Fact Integrity <br>*(Accuracy & False Claims)* | Core Edge & Advantage | Benchmark Rating |
| :--- | :--- | :--- | :--- | :--- |
| <img src="https://unpkg.com/@lobehub/icons-static-svg@latest/icons/claude-color.svg" width="20" height="20" style="vertical-align: middle; margin-right: 8px;"/> **Claude 4.7 Sonnet** | Clean three-part layout; highly formal prose that drops conversational fluff. Perfect balance of technical density and conciseness, reading like a peer-reviewed abstract. | **Near-Perfect** — accurately captures O(N²) scaling limits, database latency overhead, and prompt caching. No retrieval deviations. | Superior syntactic layout and elite editorial tone. | `█████████▋` **9.65** / 10 |
| <img src="https://unpkg.com/@lobehub/icons-static-svg@latest/icons/deepseek-color.svg" width="20" height="20" style="vertical-align: middle; margin-right: 8px;"/> **DeepSeek-R1** | Prefaces final output with an analytical thinking checklist. The final summary remains clean and compact, although the raw response log is verbose. | **High Specificity** — captures specific paper details, author names (Liu et al.), and context recall degradation curves. | Reasoning checks eliminate hallucinations. | `█████████▌` **9.55** / 10 |
| <img src="https://cdn.simpleicons.org/openai/00a67e" width="20" height="20" style="vertical-align: middle; margin-right: 8px;"/> **GPT 5.5 Instant** | Structured hierarchy containing prompt constraint checklists. Highly precise output but slightly wordier in sentence transitions. | **High Accuracy** — correctly records RAG workflow pipelines (DPR, embedding models) and native self-attention differences. | Strict execution compliance with formatting rules. | `█████████▌` **9.50** / 10 |
| <img src="https://unpkg.com/@lobehub/icons-static-svg@latest/icons/gemini-color.svg" width="20" height="20" style="vertical-align: middle; margin-right: 8px;"/> **Gemini 3.1 Pro** | Unified narrative flow linking sections together organically. However, writing style leans verbose and relies heavily on bold terms. | **High** — covers 2 million input token limits, but interprets motivations broadly rather than tracking strictly literal source facts. | Seamless global synthesis for huge context windows. | `█████████▎` **9.30** / 10 |
| <img src="https://unpkg.com/@lobehub/icons-static-svg@latest/icons/meta-color.svg" width="20" height="20" style="vertical-align: middle; margin-right: 8px;"/> **Llama 3.3 (70B)** | Bulleted list formatting. Easy to read and digest, discarding complex phrasing in favor of direct terminology. | **Moderate** — represents basic RAG vs. long-context trade-offs, but leaves out citation details and specific cost formulas. | High-speed, cost-effective standard summaries. | `████████▉░` **8.90** / 10 |

---

## 📂 Repository Structure
```text
internship-task-1/
├── README.md                           # 📖 Repository overview & guide
├── REPORT.md                           # 🔬 Benchmarking Research Paper
├── app.py                              # ⚡ Streamlit Interactive Dashboard
├── requirements.txt                    # 📦 Python project dependencies
├── data/                               # 📂 Experimentation datasets
│   ├── source_document_rag_vs_long_context.txt  # 📝 Source technical paper
│   ├── evaluation_prompt_template.txt           # 📋 Unified prompt constraints template
│   └── summaries/                      # 💾 Model Summaries
│       ├── summary_gpt_5_5_instant.txt # GPT 5.5 summary output
│       ├── summary_claude_4_7_sonnet.txt # Claude 4.7 summary output
│       ├── summary_gemini_3_1_pro.txt  # Gemini 3.1 summary output
│       ├── summary_deepseek_r1.txt     # DeepSeek-R1 summary output (with CoT logs)
│       └── summary_llama_3_3_70b.txt   # Llama 3.3 summary output
├── scripts/                            # 🛠️ Command-line utility tools
│   └── tokenizer_analysis.py           # 🔠 CLI character-to-token analyzer
└── notebooks/                          # 📓 Research environments
    └── tokenizer_exploration.py        # 🧪 Interactive notebook parsing vocabularies
```

---

## 🚀 Getting Started & Running the Suite

### 1️⃣ Set Up Your Environment
Ensure you have Python 3.12+ installed, then initialize a clean virtual environment:
```bash
# Create local virtual environment
python -m venv venv

# Activate environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install required packages
pip install -r requirements.txt
```

### 2️⃣ Run Command-Line Tokenizer Analysis
Analyze compression efficiencies and characters-per-token ratios directly in your terminal:
```bash
python scripts/tokenizer_analysis.py
```

### 3️⃣ Boot the Web Dashboard
Launch the clean Streamlit app to explore summaries, visualize tokens dynamically, and run caching economic simulations:
```bash
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser to view the interactive dashboard.

---

## ⚡ Core Insights
* 💡 **Retrieval Caching Payoff:** Prompt caching cuts cost down by **~90%** for recurrent queries, making native long-context windows cost-competitive with RAG.
* 💡 **Reasoning Frameworks:** Models like DeepSeek-R1 and GPT 5.5 Instant leverage internal reasoning tokens, achieving the highest precision flags with zero hallucinations.
* 💡 **Tokenizer Scaling:** Modern `o200k_base` model tokenizers compress text **~3.8%** more efficiently than legacy systems, reducing context footprints.
