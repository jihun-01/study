import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, average_precision_score

def calculate_map_example():
    np.random.seed(42)
    classes = ['person', 'car', 'bicycle']
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    total_ap = 0
    for i, class_name in enumerate(classes):
        n_samples = 100
        y_true = np.random.randint(0, 2, n_samples)
        y_scores = np.random.random(n_samples)
        y_scores[y_true == 1] += 0.3
        y_scores = np.clip(y_scores, 0, 1)
        precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
        ap = average_precision_score(y_true, y_scores)
        axes[0, i].plot(recall, precision, linewidth=2, label=f'AP = {ap:.3f}')
        axes[0, i].fill_between(recall, precision, alpha=0.3)
        axes[0, i].set_xlabel('Recall')
        axes[0, i].set_ylabel('Precision')
        axes[0, i].set_title(f'{class_name} - PR Curve')
        axes[0, i].legend()
        axes[0, i].grid(True, alpha=0.3)
        axes[0, i].set_xlim([0, 1])
        axes[0, i].set_ylim([0, 1])
        axes[1, i].plot(thresholds, precision[:-1], 'b-', label='Precision')
        axes[1, i].plot(thresholds, recall[:-1], 'r-', label='Recall')
        axes[1, i].set_xlabel('Confidence Threshold')
        axes[1, i].set_ylabel('Score')
        axes[1, i].set_title(f'{class_name} - Precision vs Recall')
        axes[1, i].legend()
        axes[1, i].grid(True, alpha=0.3)
        axes[1, i].set_xlim([0, 1])
        axes[1, i].set_ylim([0, 1])
        total_ap += ap
    map_score = total_ap / len(classes)
    plt.suptitle(f'mAP = {map_score:.3f}', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()
    print("클래스별 Average Precision:")
    for i, class_name in enumerate(classes):
        print(f" {class_name}: {total_ap/len(classes):.3f}")
    print(f"\nmAP: {map_score:.3f}")

calculate_map_example()
