# visualizer.py
# visualizer.py

import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# 📋 Pretty Print IOCs
def display_iocs(iocs):
    print("\n🔍 Extracted IOCs:")
    for key, values in iocs.items():
        if values:
            print(f"{key}:")
            for v in values:
                print(f"  - {v}")

# 🧠 Display action-related sentences
def display_action_sentences(sentences):
    print("\n🧠 Attack Actions:")
    for s in sentences:
        print(f"  - {s}")

# 📋 Display MITRE ATT&CK Table
def display_mitre_table(mitre_matches):
    table = [[m['tactic'], m['technique_id'], m['description']] for m in mitre_matches]
    headers = ["Tactic", "Technique ID", "Technique Description"]
    print("\n📋 MITRE ATT&CK Table:")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

# 📊 Plot Techniques by Tactic Bar Graph
def plot_techniques_by_tactic(mitre_matches):
    if not mitre_matches:
        print("\n(No MITRE mappings to plot.)")
        return
    df = pd.DataFrame(mitre_matches)
    counts = df['tactic'].value_counts()

    plt.figure(figsize=(10, 5))
    bars = plt.bar(counts.index, counts.values, color='skyblue')
    plt.title("MITRE Techniques by Tactic")
    plt.xlabel("Tactic")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, int(yval), ha='center')
    plt.tight_layout()
    plt.show()

# 🧭 Generate Mermaid Flow Graph
def generate_mermaid_diagram(mitre_matches):
    print("\n📊 Mermaid Attack Flow (Paste into mermaid.live or Markdown):\n")
    print("```mermaid")
    print("graph TD")
    prev = None
    for i, m in enumerate(mitre_matches):
        node = chr(65 + i)
        label = f"{m['tactic']}: {m['description']} ({m['technique_id']})"
        print(f"  {node}[{label}]")
        if prev:
            print(f"  {prev} --> {node}")
        prev = node
    print("```")
To use this in main.py, just import the functions like this:
from visualizer import (
    display_iocs,
    display_action_sentences,
    display_mitre_table,
    plot_techniques_by_tactic,
    generate_mermaid_diagram
)
