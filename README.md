تمام يا بطل! ✅ راح أعدل لك كل الروابط الوهمية إلى روابطك الحقيقية وأحول المحتوى إلى الإنجليزية.

---

⚔️ W-GHOST - Professional Vulnerability Scanning Tool ⚔️

<div align="center">

https://img.shields.io/badge/W--GHOST-Security%20Scanner-red?style=for-the-badge
https://img.shields.io/badge/Version-1.0.0-green?style=flat-square
https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python
https://img.shields.io/badge/License-MIT-yellow?style=flat-square
https://img.shields.io/badge/Platform-Termux-orange?style=flat-square&logo=android
https://img.shields.io/github/stars/Emaf-png/W-GHOST?style=social

Advanced Vulnerability Assessment Tool - Termux Edition

Features • Installation • Usage • Developer

</div>

---

📖 Overview

W-GHOST is a professional-grade vulnerability scanning tool designed specifically for Termux on Android devices. Built for cybersecurity students and network security researchers, it provides an intuitive interface with advanced network scanning and vulnerability detection capabilities.

👨‍💻 Developer: Emad Zawawid (عماد الزواوي)

---

✨ Features

Category Capabilities
🔍 Port Scanning SYN Scan, TCP/UDP detection, Service version identification, Top 1000 ports
🖥️ OS Detection OS fingerprinting, Version guessing, Accuracy percentage
⚠️ Vulnerability Assessment NSE scripts, CVE detection, Vulners database support, Detailed reports
📊 Reporting Structured tables, TXT export, JSON export, Auto-timestamped reports
🎨 UI/UX Colored interface, Progress indicator, Professional ASCII logo

---

🚀 Installation

Prerequisites (Termux)

```bash
# Update base packages
pkg update && pkg upgrade -y

# Install dependencies
pkg install python python-pip nmap git -y
```

Clone & Setup

```bash
# Clone the repository
git clone https://github.com/Emaf-png/W-GHOST.git

# Navigate to the tool directory
cd W-GHOST

# Install Python libraries
pip install -r requirements.txt

# Make the script executable
chmod +x w-ghost.py
```

requirements.txt

```
python-nmap>=0.6.1
colorama>=0.4.4
tabulate>=0.8.9
argparse>=1.4.0
```

---

📚 Usage

Basic Syntax

```bash
python w-ghost.py -t <target> [-o <output_name>] [-f <format>]
```

Command Options

Option Description
-t, --target Target IP, domain, or network range (Required)
-o, --output Save report with specified name
-f, --format Report format: txt or json (default: txt)

Practical Examples

```bash
# Scan a single IP
python w-ghost.py -t 192.168.1.1

# Scan a domain with report
python w-ghost.py -t example.com -o scan_result

# Scan with JSON export
python w-ghost.py -t 10.0.0.1 -o report -f json

# Scan an entire subnet
python w-ghost.py -t 192.168.1.0/24

# Scan with root privileges (better results)
tsu -c "python w-ghost.py -t 192.168.1.1"
```

---

📸 Screenshots

⭐ Startup Screen

```
██╗    ██╗       ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
██║    ██║      ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
██║ █╗ ██║█████╗██║  ███╗███████║██║   ██║███████╗   ██║   
██║███╗██║╚════╝██║   ██║██╔══██║██║   ██║╚════██║   ██║   
╚███╔███╔╝      ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
 ╚══╝╚══╝        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   

              ╔══════════════════════════════════════════╗
              ║       PROFESSIONAL VULNERABILITY          ║
              ║            SCANNING TOOL                  ║
              ╚══════════════════════════════════════════╝

                   Developed by Emad Zawawid
```

📊 Scan Results

```
[+] Target: 192.168.1.1
[+] Hostname: router.local
[+] State: up

┌──────┬──────────┬────────┬─────────┬─────────────────┐
│ Port │ Protocol │ State  │ Service │ Version         │
├──────┼──────────┼────────┼─────────┼─────────────────┤
│ 22   │ TCP      │ open   │ ssh     │ OpenSSH 7.9     │
│ 80   │ TCP      │ open   │ http    │ Apache 2.4.38   │
│ 443  │ TCP      │ open   │ https   │ nginx 1.14.2    │
│ 3306 │ TCP      │ open   │ mysql   │ MySQL 5.7.32    │
└──────┴──────────┴────────┴─────────┴─────────────────┘

[ OS Detection ]
┌─────────────────────┬────────────┐
│ OS Match            │ Accuracy   │
├─────────────────────┼────────────┤
│ Linux 3.2 - 4.9     │ 95%        │
└─────────────────────┴────────────┘
```

---

🗂️ Project Structure

```
W-GHOST/
├── w-ghost.py              # Main tool script
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── LICENSE               # MIT License
└── reports/              # Scan reports (auto-generated)
```

---

🛠️ Technologies Used

Library Purpose
python-nmap Nmap Python interface
colorama Terminal text coloring
tabulate Structured table display
argparse CLI argument parsing
threading Parallel processing
json Report export

---

⚠️ Legal Disclaimer

```
⚠️ IMPORTANT ⚠️

This tool is for EDUCATIONAL AND RESEARCH PURPOSES ONLY.

❌ DO NOT scan systems without explicit permission
❌ DO NOT use for illegal activities
❌ The developer is NOT responsible for misuse

✅ ONLY use on your own devices
✅ ONLY use in lab environments for learning
✅ ALWAYS obtain written authorization before scanning
```

---

🐛 Common Issues & Solutions

<details>
<summary><b>Issue: "nmap not found"</b></summary>

```bash
pkg install nmap -y
```

</details>

<details>
<summary><b>Issue: "Permission denied"</b></summary>

```bash
chmod +x w-ghost.py
# Or use root
tsu
```

</details>

<details>
<summary><b>Issue: Slow scanning</b></summary>

```python
# Modify scan arguments for speed
arguments='-T5'  # Faster timing template
arguments='--top-ports 100'  # Fewer ports
```

</details>

---

🤝 Contributing

We welcome contributions! Follow these steps:

```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/Emaf-png/W-GHOST.git

# 3. Create a feature branch
git checkout -b feature/amazing-feature

# 4. Commit your changes
git add .
git commit -m "✨ Add amazing feature"

# 5. Push to GitHub
git push origin feature/amazing-feature

# 6. Open a Pull Request
```

---

📈 Roadmap

· GUI Interface
· Web Application Scanning
· More NSE Scripts
· Database Vulnerability Checks
· HTML Report Export
· Notification System
· Scheduled Scanning

---

📄 License

This project is licensed under the MIT License.

```txt
MIT License

Copyright (c) 2024 Emad Zawawid

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

📞 Contact & Support

<div align="center">

https://img.shields.io/badge/GitHub-Emaf--png-black?style=for-the-badge&logo=github
https://img.shields.io/badge/Telegram-EMAD__Di-blue?style=for-the-badge&logo=telegram

</div>

---

⭐ Show Your Support

If you find this project useful, please:

· ⭐ Star it on GitHub
· 📢 Share with fellow cybersecurity enthusiasts
· 🐛 Report bugs in Issues
· 🤝 Contribute via Pull Requests

---

<div align="center">

Made with ❤️ by Emad Zawawid | © 2024 All Rights Reserved

https://img.shields.io/badge/GitHub-Emaf--png-black?style=for-the-badge&logo=github
https://img.shields.io/badge/Telegram-EMAD__Di-blue?style=for-the-badge&logo=telegram

</div>
```

---

✅ Summary of Changes:

Before (Fake) After (Real)
via.placeholder.com Removed completely
github.com/EmadZawawid github.com/Emaf-png
your.email@example.com Removed (Telegram is enough)
t.me/yourchannel t.me/EMAD_Di
Arabic text Full English translation
Fake badge links Real GitHub badges

---

🚀 Quick Deploy to GitHub:

```bash
# Save the README
nano README.md
# Paste the content above, Ctrl+X, Y, Enter

# Commit and push
git add README.md
git commit -m "📝 Update README with real links and English translation"
git push origin main
```

· GitHub: github.com/Emaf-png
· Telegram: t.me/EMAD_Di

