# mitre_data.py
# 🎯 MITRE ATT&CK Keyword to Technique Mapping
mitre_map = {
    "phishing": ("Initial Access", "T1566.001", "Spearphishing Attachment"),
    "macro": ("Execution", "T1059.005", "Command & Scripting Interpreter: VBScript"),
    "powershell": ("Execution", "T1059.001", "PowerShell"),
    "registry": ("Persistence", "T1547.001", "Registry Run Keys / Startup Folder"),
    "service": ("Persistence", "T1543.003", "Create or Modify System Process: Windows Service"),
    "https": ("Exfiltration", "T1041", "Exfiltration Over HTTPS"),
    "c2": ("Command and Control", "T1071.001", "Web Protocols"),
    "beacon": ("Command and Control", "T1071.001", "Web Protocols"),
    "mimikatz": ("Credential Access", "T1003", "OS Credential Dumping"),
    "credential": ("Credential Access", "T1003", "Credential Dumping"),
    "command": ("Execution", "T1059", "Command and Scripting Interpreter"),
    "download": ("Execution", "T1204.002", "User Execution: Malicious File"),
    "execute": ("Execution", "T1203", "Exploitation for Client Execution"),
    "exfiltrate": ("Exfiltration", "T1041", "Exfiltration Over HTTPS")
}

This file can now be imported into your main script like this:
from mitre_data import mitre_map
