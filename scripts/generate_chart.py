#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# Adjust global settings for a premium, clean look
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#4A3E3D'
plt.rcParams['axes.labelcolor'] = '#4A3E3D'
plt.rcParams['xtick.color'] = '#6D5E5D'
plt.rcParams['ytick.color'] = '#6D5E5D'
plt.rcParams['figure.facecolor'] = '#F9F6F0'  # Soft light cream/skin background
plt.rcParams['axes.facecolor'] = '#F9F6F0'

# Data
models = [
    "Claude 4.7\nOpus", 
    "DeepSeek\nV4", 
    "GPT 5.5\nInstant", 
    "Gemini 3.1\nPro", 
    "Llama 3.3\n(70B)"
]
scores = [9.65, 9.55, 9.50, 9.30, 8.90]  # Weighted overall scores from the main comparative table

# Create the figure
fig, ax = plt.subplots(figsize=(8, 5.5), dpi=300)

# Colors: a refined, warm organic palette (earth tones)
colors = ['#C86A5A', '#6D8294', '#D4A373', '#9CA986', '#BCA3AC']

# Plot bars with a clean flat style
bars = ax.bar(models, scores, color=colors, width=0.5, edgecolor='none', zorder=3)

# Grid - very subtle and minimal
ax.grid(axis='y', linestyle='--', alpha=0.4, color='#CABCB6', zorder=0)

# Remove axes spines (borders) for a modern, open feel
for spine in ['top', 'right', 'left', 'bottom']:
    ax.spines[spine].set_visible(False)

# Configure the Y-axis to start at 0 to keep the comparison fair and proportional
ax.set_ylim(0, 11)
ax.set_ylabel("Overall Benchmark Rating (Out of 10.0)", fontsize=11, fontweight='500', labelpad=12)

# Set title
ax.set_title("LLM Summarization Benchmarking Standings\n(Weighted Synthesis Performance Matrix)", 
             fontsize=13, fontweight='bold', pad=25, color='#3B2F2E')

# Add rating labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 6),  # 6 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', 
                fontsize=10.5, fontweight='bold', 
                color='#3B2F2E')

# Adjust layout to prevent clipping of labels
plt.tight_layout()

# Save the plot
output_path = "llm_comparison_chart.png"
plt.savefig(output_path, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
print(f"✅ Minimalistic, fair visual chart saved successfully to {output_path}")
