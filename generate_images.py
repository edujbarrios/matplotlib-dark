"""
Generate theme comparison image for README - ML/DL Training Visualizations
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib_dark as mdk

# Create images directory if it doesn't exist
import os
os.makedirs('images', exist_ok=True)

print("Generating theme comparison image...")

np.random.seed(42)

# Create figure with dark background
fig = plt.figure(figsize=(16, 12), facecolor='#1e1e1e')
fig.suptitle('Dark Theme Spectrum - ML/DL Training Visualizations', fontsize=20, fontweight='bold', color='#e4e4e4')

# 1. DEFAULT - Training Loss Curves
mdk.set_theme('default')
ax1 = plt.subplot(3, 2, 1)
ax1.set_facecolor(plt.rcParams['axes.facecolor'])
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
epochs = np.arange(1, 101)
train_loss = 2.5 * np.exp(-epochs / 20) + 0.1 + np.random.normal(0, 0.05, 100)
val_loss = 2.5 * np.exp(-epochs / 20) + 0.15 + np.random.normal(0, 0.08, 100)
ax1.plot(epochs, train_loss, linewidth=2.5, label='Training Loss', color=colors[0])
ax1.plot(epochs, val_loss, linewidth=2.5, label='Validation Loss', color=colors[1])
ax1.set_title('Default Theme - Training Loss', fontsize=12, fontweight='bold', color=plt.rcParams['text.color'])
ax1.legend(loc='upper right', fontsize=9, facecolor=plt.rcParams['axes.facecolor'], edgecolor=plt.rcParams['grid.color'], labelcolor=plt.rcParams['text.color'])
ax1.grid(True, alpha=0.3, color=plt.rcParams['grid.color'])
ax1.tick_params(colors=plt.rcParams['text.color'])
for spine in ax1.spines.values():
    spine.set_color(plt.rcParams['text.color'])
ax1.set_xlabel('Epoch', fontsize=9, color=plt.rcParams['text.color'])
ax1.set_ylabel('Loss', fontsize=9, color=plt.rcParams['text.color'])

# 2. NORD - Accuracy Metrics
mdk.set_theme('nord')
ax2 = plt.subplot(3, 2, 2)
ax2.set_facecolor(plt.rcParams['axes.facecolor'])
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
train_acc = 1 - np.exp(-epochs / 15) * 0.8 - np.random.normal(0, 0.01, 100)
val_acc = 1 - np.exp(-epochs / 15) * 0.85 - np.random.normal(0, 0.015, 100)
test_acc = 1 - np.exp(-epochs / 15) * 0.87 - np.random.normal(0, 0.012, 100)
ax2.plot(epochs, train_acc, linewidth=2.5, label='Train', color=colors[0])
ax2.plot(epochs, val_acc, linewidth=2.5, label='Validation', color=colors[1])
ax2.plot(epochs, test_acc, linewidth=2.5, label='Test', color=colors[2], linestyle='--')
ax2.set_title('Nord Theme - Accuracy Curves', fontsize=12, fontweight='bold', color=plt.rcParams['text.color'])
ax2.legend(loc='lower right', fontsize=9, facecolor=plt.rcParams['axes.facecolor'], edgecolor=plt.rcParams['grid.color'], labelcolor=plt.rcParams['text.color'])
ax2.grid(True, alpha=0.3, color=plt.rcParams['grid.color'])
ax2.tick_params(colors=plt.rcParams['text.color'])
for spine in ax2.spines.values():
    spine.set_color(plt.rcParams['text.color'])
ax2.set_xlabel('Epoch', fontsize=9, color=plt.rcParams['text.color'])
ax2.set_ylabel('Accuracy', fontsize=9, color=plt.rcParams['text.color'])
ax2.set_ylim(0.15, 1.0)

# 3. MONOKAI - Model Comparison
mdk.set_theme('monokai')
ax3 = plt.subplot(3, 2, 3)
ax3.set_facecolor(plt.rcParams['axes.facecolor'])
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
models = ['ResNet50', 'VGG16', 'EfficientNet', 'MobileNet', 'DenseNet', 'Inception']
accuracies = [94.2, 92.1, 95.8, 91.5, 93.7, 94.5]
bars = ax3.bar(models, accuracies, color=colors[:6], alpha=0.8, edgecolor='white', linewidth=1)
for bar, acc in zip(bars, accuracies):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 0.5, f'{acc:.1f}%',
            ha='center', va='bottom', fontsize=8, color=plt.rcParams['text.color'])
ax3.set_title('Monokai Theme - Model Performance', fontsize=12, fontweight='bold', color=plt.rcParams['text.color'])
ax3.grid(True, alpha=0.3, axis='y', color=plt.rcParams['grid.color'])
ax3.tick_params(colors=plt.rcParams['text.color'], axis='x', rotation=45)
plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45, ha='right', fontsize=8)
for spine in ax3.spines.values():
    spine.set_color(plt.rcParams['text.color'])
ax3.set_ylabel('Accuracy (%)', fontsize=9, color=plt.rcParams['text.color'])
ax3.set_ylim(88, 97)

# 4. DRACULA - Learning Rate Schedule
mdk.set_theme('dracula')
ax4 = plt.subplot(3, 2, 4)
ax4.set_facecolor(plt.rcParams['axes.facecolor'])
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
# Different LR schedules
lr_constant = np.ones(100) * 0.001
lr_step = np.where(epochs < 30, 0.01, np.where(epochs < 60, 0.001, 0.0001))
lr_exp = 0.01 * np.exp(-epochs / 30)
lr_cosine = 0.01 * (1 + np.cos(np.pi * epochs / 100)) / 2
ax4.plot(epochs, lr_constant, linewidth=2.5, label='Constant', color=colors[0])
ax4.plot(epochs, lr_step, linewidth=2.5, label='Step Decay', color=colors[1])
ax4.plot(epochs, lr_exp, linewidth=2.5, label='Exponential', color=colors[2])
ax4.plot(epochs, lr_cosine, linewidth=2.5, label='Cosine Annealing', color=colors[3])
ax4.set_title('Dracula Theme - Learning Rate Schedules', fontsize=12, fontweight='bold', color=plt.rcParams['text.color'])
ax4.legend(loc='upper right', fontsize=9, facecolor=plt.rcParams['axes.facecolor'], edgecolor=plt.rcParams['grid.color'], labelcolor=plt.rcParams['text.color'])
ax4.grid(True, alpha=0.3, color=plt.rcParams['grid.color'])
ax4.tick_params(colors=plt.rcParams['text.color'])
ax4.set_yscale('log')
for spine in ax4.spines.values():
    spine.set_color(plt.rcParams['text.color'])
ax4.set_xlabel('Epoch', fontsize=9, color=plt.rcParams['text.color'])
ax4.set_ylabel('Learning Rate', fontsize=9, color=plt.rcParams['text.color'])

# 5. NEON - Multi-Metric Training
mdk.set_theme('neon')
ax5 = plt.subplot(3, 2, 5)
ax5.set_facecolor(plt.rcParams['axes.facecolor'])
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
precision = 0.7 + 0.25 * (1 - np.exp(-epochs / 20)) + np.random.normal(0, 0.01, 100)
recall = 0.65 + 0.3 * (1 - np.exp(-epochs / 18)) + np.random.normal(0, 0.012, 100)
f1_score = 2 * (precision * recall) / (precision + recall)
auc = 0.75 + 0.2 * (1 - np.exp(-epochs / 22)) + np.random.normal(0, 0.008, 100)
ax5.plot(epochs, precision, linewidth=2.5, label='Precision', color=colors[0], alpha=0.9)
ax5.plot(epochs, recall, linewidth=2.5, label='Recall', color=colors[1], alpha=0.9)
ax5.plot(epochs, f1_score, linewidth=2.5, label='F1-Score', color=colors[2], alpha=0.9)
ax5.plot(epochs, auc, linewidth=2.5, label='AUC-ROC', color=colors[3], alpha=0.9)
ax5.set_title('Neon Theme - Classification Metrics', fontsize=12, fontweight='bold', color=plt.rcParams['text.color'])
ax5.legend(loc='lower right', fontsize=9, facecolor=plt.rcParams['axes.facecolor'], edgecolor=plt.rcParams['grid.color'], labelcolor=plt.rcParams['text.color'])
ax5.grid(True, alpha=0.2, color=plt.rcParams['grid.color'])
ax5.tick_params(colors=plt.rcParams['text.color'])
for spine in ax5.spines.values():
    spine.set_color(plt.rcParams['text.color'])
ax5.set_xlabel('Epoch', fontsize=9, color=plt.rcParams['text.color'])
ax5.set_ylabel('Score', fontsize=9, color=plt.rcParams['text.color'])
ax5.set_ylim(0.6, 1.0)

# 6. MATERIAL - Training Time Comparison
mdk.set_theme('material')
ax6 = plt.subplot(3, 2, 6)
ax6.set_facecolor(plt.rcParams['axes.facecolor'])
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
batch_sizes = [16, 32, 64, 128, 256]
training_times = [245, 156, 98, 67, 52]  # minutes
memory_usage = [8.2, 12.5, 18.9, 26.3, 31.8]  # GB
ax6_twin = ax6.twinx()
bars = ax6.bar(batch_sizes, training_times, color=colors[0], alpha=0.8, width=20, label='Training Time')
line = ax6_twin.plot(batch_sizes, memory_usage, color=colors[4], marker='o', linewidth=2.5, 
                      markersize=8, label='Memory Usage')
ax6.set_title('Material Theme - Batch Size Analysis', fontsize=12, fontweight='bold', color=plt.rcParams['text.color'])
ax6.set_xlabel('Batch Size', fontsize=9, color=plt.rcParams['text.color'])
ax6.set_ylabel('Training Time (min)', fontsize=9, color=plt.rcParams['text.color'])
ax6_twin.set_ylabel('Memory Usage (GB)', fontsize=9, color=plt.rcParams['text.color'])
ax6.grid(True, alpha=0.3, color=plt.rcParams['grid.color'])
ax6.tick_params(colors=plt.rcParams['text.color'])
ax6_twin.tick_params(colors=plt.rcParams['text.color'])
for spine in ax6.spines.values():
    spine.set_color(plt.rcParams['text.color'])
for spine in ax6_twin.spines.values():
    spine.set_color(plt.rcParams['text.color'])
# Combined legend
lines1, labels1 = ax6.get_legend_handles_labels()
lines2, labels2 = ax6_twin.get_legend_handles_labels()
ax6.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=9,
          facecolor=plt.rcParams['axes.facecolor'], edgecolor=plt.rcParams['grid.color'], 
          labelcolor=plt.rcParams['text.color'])

plt.tight_layout()
plt.savefig('images/theme_comparison.png', dpi=150, bbox_inches='tight', facecolor='#1e1e1e')
plt.close()

print("✓ Theme comparison image generated successfully!")
mdk.light_mode()

