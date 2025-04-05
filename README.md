🧠 CTI_Report — AI-Powered Cyber Threat Intelligence Analyzer
CTI_Report is a lightweight, Python-based tool that uses AI and automation to extract and analyze cybersecurity threat intelligence from text reports. It identifies Indicators of Compromise (IOCs), maps them to the MITRE ATT&CK framework, and visualizes the attack chain — all without needing any external tools or online services.

🚀 Key Features
📝 Smart Text Parsing
Automatically analyzes raw cybersecurity reports to detect and extract:

✅ IP addresses

✅ Domains & URLs

✅ File hashes (MD5, SHA1, SHA256)

✅ Other critical IOCs

🎯 MITRE ATT&CK Mapping
Maps attack-related text to MITRE ATT&CK Tactics and Techniques

Uses keyword matching and pattern recognition

Helps you understand attacker behavior at a glance

📊 Visual Insights
Your data comes to life with powerful built-in visualizations:

IOC Table – Clean table of all detected IOCs using tabulate

Technique-by-Tactic Chart – Simple bar graph with matplotlib

Attack Flow Graph – Visual diagram of the full attack chain using networkx

🧪 Built-in Testing
Designed to handle all types of input:

✅ Clean, structured cyber reports

✅ Messy or incomplete reports (error-resilient parsing)

🛠 Tech Stack
Tool/Library	Purpose
Python 3.x	Core programming language
re	Regex-based IOC extraction
matplotlib	Charts and visualizations
pandas	Data handling for plots/tables
networkx	Attack graph visualizations
tabulate	Clean console tables

⚙️ How It Works
Input: Load or paste a plaintext cyber threat report.

Extraction: Script identifies all IOCs using regex.

MITRE Mapping: Descriptions are matched to MITRE techniques.

Output:

IOC summary table

MITRE tactic-technique chart

Directed graph of attack flow

🎯 Example Output (Visualized)
IPs: 192.168.10.45, 91.240.118.221

Technique: Command and Control → T1071.001 (Web Protocols)

Chart: Bar graph of tactics

Graph: Node-link diagram of attack path
