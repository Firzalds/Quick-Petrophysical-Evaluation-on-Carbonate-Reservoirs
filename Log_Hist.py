import pandas as pd
import matplotlib.pyplot as plt


def calculate_statistics(df, columns):
    stats = {}
    for col in columns:
        mean_value = df[col].mean()
        p5_value = df[col].quantile(0.05)
        p95_value = df[col].quantile(0.95)

        stats[col] = {
            'Mean': mean_value,
            'P05': p5_value,
            'P95': p95_value
        }

    return pd.DataFrame(stats).T  

def plot_histograms(df, columns, bins=30):
    n_cols = 3  
    n_rows = -(-len(columns) // n_cols)
    colors = ['cyan','teal' , 'orange', 'red','yellow','pink','gray', 'olive', 'lime']
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 5, n_rows * 4))
    axes = axes.flatten() 

    for i, col in enumerate(columns):
        mean_value = df[col].mean()
        p5_value = df[col].quantile(0.05)
        p95_value = df[col].quantile(0.95)

        color = colors[i % len(colors)]  

        axes[i].hist(df[col], bins=bins, color=color, alpha=0.6, edgecolor='black')
        axes[i].axvline(mean_value, color='blue', linestyle='-', label='Mean')
        axes[i].axvline(p5_value, color='green', linestyle='--', label='5th Percentile')
        axes[i].axvline(p95_value, color='purple', linestyle='--', label='95th Percentile')
        
        axes[i].set_xlabel(col, fontsize=12)
        axes[i].set_ylabel('Frequency', fontsize=12)
        axes[i].set_title(f'{col} histogram', fontsize=14)
        axes[i].legend()
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()  
    plt.show()

