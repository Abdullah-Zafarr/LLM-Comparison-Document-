import streamlit as st
import pandas as pd
import plotly.express as px
import tiktoken
import html
import os

# Set page configuration
st.set_page_config(
    page_title="LLM Comparison & Tokenization Benchmarking",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Grounded & Professional Styling)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.2rem;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #64748B;
        margin-bottom: 2rem;
    }
    
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #0F172A;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }

    .card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
    }
    
    .token-container {
        font-family: monospace;
        line-height: 2.0;
        padding: 15px;
        border-radius: 8px;
        background-color: #0F172A;
        color: #F8FAFC;
# Stubs for tabs will be added next
