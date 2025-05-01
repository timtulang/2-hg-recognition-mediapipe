import pandas as pd
import matplotlib.pyplot as plt
import sys

def main():
    # Check for file input
    if len(sys.argv) != 2:
        print("Usage: python analyze_distribution.py <path_to_csv>")
        return

    csv_file = sys.argv[1]

    # Load CSV (no header)
    try:
        df = pd.read_csv(csv_file, header=None)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    # Assume first column is the label/index
    labels = df[0]

    # Count label occurrences
    label_counts = labels.value_counts().sort_index()

    # Print distribution stats
    print("Label Distribution:\n", label_counts, "\n")
    print(f"Number of unique labels: {labels.nunique()}")
    print(f"Total samples: {len(labels)}")
    print(f"Min samples in a class: {label_counts.min()}")
    print(f"Max samples in a class: {label_counts.max()}")
    print(f"Standard deviation of class counts: {label_counts.std():.2f}")

    # Plot bar chart
    plt.figure(figsize=(10, 5))
    label_counts.plot(kind='bar')
    plt.xlabel("Class Index")
    plt.ylabel("Frequency")
    plt.title("Label Distribution")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
