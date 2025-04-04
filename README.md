# CTI_Report
 🔐 AI-Powered Cyber Threat Intelligence Analyzer
This project is a lightweight, AI-assisted cyber threat analysis tool that extracts key Indicators of Compromise (IOCs) from textual threat reports and maps them to the MITRE ATT&CK framework. It also visualizes the attack flow using Python libraries — no external websites or tools needed.

🚀 Features
📄 Text Analysis: Parse raw cyber reports to identify IOCs like IPs, domains, URLs, file hashes, and more.

🎯 MITRE Mapping: Automatically map textual attack descriptions to corresponding MITRE ATT&CK techniques and tactics.

📊 Visualizations:

IOC Table (using tabulate)

Technique-by-Tactic Bar Graph (with matplotlib)

Full Attack Flow Graph (with networkx)

🧪 Robust Testing with:

Clean sample reports

Malformed/broken reports (to test error handling)

🛠 Technologies Used
Python 3.x

re for regex-based IOC extraction

matplotlib and pandas for graphs and tables

networkx for attack chain diagrams

tabulate for clean console output

📂 Project Structure
bash
Copy
Edit
├── main.py                  # Main script to run everything
├── mitre_data.py            # Sample data mapping keywords to MITRE techniques
├── visualizer.py            # Module for all graphs/tables/diagrams
├── sample_report.txt        # Example cyber report (you can modify this)
📌 How It Works
Paste or load a cyber report (plaintext).

The script extracts:

IPs

Domains

URLs

MD5/SHA1/SHA256 hashes

Matches lines to known MITRE techniques using keyword matching.

Displays:

A summary table of all techniques and tactics

A tactic-vs-technique bar chart

A full attack flow using a directed graph

