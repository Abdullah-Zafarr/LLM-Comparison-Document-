# 🤖 AI Engineering Lab: LLM Summarization Benchmarking & Tokenization Study

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
</p>

Welcome to the **LLM Benchmarking & Tokenization Analysis** workspace! This laboratory repository evaluates and compares structural accuracy, tokenization efficiency, and deployment economics of Large Language Models (LLMs) on document summarization, comparing traditional **Retrieval-Augmented Generation (RAG)** systems against native **Long-Context Window** models.

We analyze five modern cognitive architectures: **GPT 5.5 Instant**, **Claude 4.7 Sonnet**, **Gemini 3.1 Pro**, **DeepSeek-R1**, and **Llama 3.3 (70B)**.

---

## 🎨 Feature Comparison Dashboard
We evaluate and rank each model on the document summarization task across four critical dimensions:

### 📊 Model Performance Evaluation Matrix

| Model | Summary Quality | Accuracy | Conciseness | Hallucinations | Overall Score |
| :--- | :--- | :--- | :--- | :--- | :---: |
| <img src="https://img.icons8.com/color/24/artificial-intelligence.png"/> **Claude 4.7 Sonnet** | Clean three-part structure, highly formal and analytical tone. Bypasses introductory filler entirely. | **Very High** — correctly captures execution trade-offs, $O(N^2)$ attention scaling limits, prompt caching cost models, and retriever dependencies. | **Outstanding** — highly descriptive yet compact, avoiding verbose elaboration while retaining technical terminologies. | **None detected** — all claims, cited parameters, and mathematical metrics map directly to the source. | **9.65 / 10** |
| <img src="https://img.icons8.com/fluency/24/brainstorm.png"/> **DeepSeek-R1** | Employs reinforcement-learning guided reasoning checklist. Well-formatted with three clear structural sections. | **Very High** — includes specific citation structures (such as the "Lost in the Middle" study by Liu et al.) and details attention bottlenecks. | **High** — extremely concise final output, though the raw response includes a verbose internal chain-of-thought log. | **None detected** — thinking checklist successfully guards against semantic hallucination. | **9.55 / 10** |
| <img src="https://img.icons8.com/color/24/openai.png"/> **GPT 5.5 Instant** | Clean structure featuring a simulated constraint checklist. Highly precise and abstract-like presentation. | **Very High** — correctly identifies architectural components of RAG (DPR, vector DB indexing) and needle-in-a-haystack limits. | **High** — slightly more wordy than Claude but structured nicely with cohesive takeaways and summaries. | **None detected** — maintains strict alignment with source document claims. | **9.50 / 10** |
| <img src="https://img.icons8.com/color/24/google-logo.png"/> **Gemini 3.1 Pro** | Well-structured, excellent explanatory flow, transition between sections is highly natural and narrative. | **High** — correctly references large context windows (2M tokens) and maps RAG workflow details (k-NN search, embeddings). | **Moderate** — slightly more explanatory and verbose, especially when discussing tokenization advantages. | **Subtle** — borderline interpretive framing of motivations, but stays strictly within context bounds. | **9.30 / 10** |
| <img src="https://img.icons8.com/color/24/meta-logo.png"/> **Llama 3.3 (70B)** | Clean, bulleted breakdown, directly readable. Excellent formatting for quick summaries. | **Moderate** — accurately captures RAG vs. long-context trade-offs, though it leaves out specific researcher names and citations. | **High** — high efficiency in word usage, directly getting to the core differences in system maintenance. | **Minor** — generalized context statements but no factual discrepancies. | **8.90 / 10** |

---

## 📂 Repository Structure
```text
internship-task-1/
├── README.md                           # 📖 Colorful repository overview & guide
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
