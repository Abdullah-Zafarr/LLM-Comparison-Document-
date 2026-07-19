# 🤖 AI Engineering Lab: LLM Summarization Benchmarking & Tokenization Study

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org)
[![Streamlit App](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io)
[![Model Comparison](https://img.shields.io/badge/Architectures-RAG%20vs%20Long--Context-purple.svg)](#)

Welcome to the **LLM Benchmarking & Tokenization Analysis** study suite. This repository evaluates the trade-offs of deploying Large Language Models (LLMs) on document summarization tasks, specifically contrasting **Retrieval-Augmented Generation (RAG)** systems with native **Long-Context Window** ingestion.

This project compares modern frontier architectures (**GPT 5.5 Instant**, **Claude 4.7 Sonnet**, **Gemini 3.1 Pro**, **DeepSeek-R1**, and **Llama 3.3 70B**), exploring tokenizers, and simulating caching economics.

---

## 🌟 Key Features
1. **Model Evaluation:** Summarization comparisons across multiple top LLM providers using the exact same evaluation inputs and prompt template constraints.
2. **Interactive Tokenizer Visualizer:** A Streamlit dashboard showing how characters map color-coded to token boundaries for GPT-4 (`cl100k_base`) vs GPT-4o/o1/GPT 5.5 (`o200k_base`).
3. **Economics & Caching Simulator:** A mathematical analysis representing monthly expenditure comparison between standard RAG retrieval and Long-Context direct loading utilizing server prompt caching.

---

## 📂 Repository Structure
```text
internship-task-1/
├── README.md                           # Main engineering overview & guide
├── REPORT.md                           # Research & Summarization Paper
├── app.py                              # Streamlit Benchmark Dashboard
├── requirements.txt                    # Project dependencies
├── data/                               # Experimentation datasets
│   ├── source_document_rag_vs_long_context.txt  # Technical paper compiled for benchmarking
│   ├── evaluation_prompt_template.txt           # Unified instructions prompt
│   └── summaries/                      # Generated model summaries
│       ├── summary_gpt_5_5_instant.txt # GPT 5.5 Instant summary output
│       ├── summary_claude_4_7_sonnet.txt # Claude 4.7 Sonnet summary output
│       ├── summary_gemini_3_1_pro.txt  # Gemini 3.1 Pro summary output
│       ├── summary_deepseek_r1.txt     # DeepSeek-R1 summary output (with thinking logs)
│       └── summary_llama_3_3_70b.txt   # Llama 3.3 70B summary output
├── scripts/                            # CLI analysis tools
│   └── tokenizer_analysis.py           # Analysis script comparing token efficiencies
└── notebooks/
    └── tokenizer_exploration.py        # Exploration script mapping token boundaries
```

---

## 📊 Benchmarked Models Specifications

| Model Name | Creator | Context Window | Vocabulary Size | Key Architectural Specialty |

Setup instructions to follow...