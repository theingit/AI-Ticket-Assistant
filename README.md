# AI Ticket Assistant (Python)

A Python-based AI Ticket Assistant for ITSM ticket validation, classification, impact analysis, and operational reporting.

## Overview

AI Ticket Assistant is a Python command-line application designed to support IT operations and application support activities.

The application can:

- Read tickets exported from an ITSM system
- Validate and parse ticket records
- Categorize tickets
- Determine potential business impact
- Generate reports with recommended actions

This project simulates real-world operational support tasks performed by Application Support Engineers and Production Support Engineers.

## Key Features

- **Ticket Import** – Reads ticket records from CSV files
- **Ticket Validation** – Checks ticket data for missing or invalid values
- **Ticket Classification** – Categorizes tickets based on their information
- **Impact Analysis** – Determines the potential operational impact
- **Recommended Actions** – Suggests an appropriate action based on ticket priority and impact
- **Operational Reporting** – Generates a summary of ticket information for support teams

## Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub
- Python Standard Library (`csv`, `pathlib`, `collections`)

## Project Structure

```text
AI_Ticket_Assistant/
│
├── data/
│   └── tickets.csv
│
├── src/
│   └── read_tickets.py
│
└── README.md

How to Run
1. Clone the repository
git clone https://github.com/theingit/AI-Ticket-Assistant.git

2. Move into the project directory
cd AI_Ticket_Assistant

3. Run the application
python src/read_tickets.py

Sample Output
==================================
 AI Ticket Assistant v0.2
==================================

Ticket Summary
--------------------------------
Total Tickets : 4
High Priority : 1
Medium        : 2
Low           : 1
--------------------------------

Ticket ID           : INC-1001
Priority            : High
Application         : Payment System
Category            : Payment Issue
Potential Impact    : Critical
Recommended Action  : Escalate immediately

Description         :
Users are unable to submit payment transactions. The application returns an error after clicking Submit.

Ticket ID           : INC-1002
Priority            : Medium
Application         : HR Portal
Category            : HR / Payroll
Potential Impact    : Medium
Recommended Action  : Investigate within normal SLA

Description         :
User cannot download the monthly payslip from the HR portal.

Ticket ID           : INC-1003
Priority            : Low
Application         : Email System
Category            : Email Support
Potential Impact    : Low
Recommended Action  : Handle as standard service request

Description         :
User requested assistance with configuring an email signature.

Ticket ID           : INC-1004
Priority            : Medium
Application         : ERP
Category            : ERP System Issue
Potential Impact    : High
Recommended Action  : Prioritize for investigation

Description         :
Users are unable to view orders.

Future Improvements
Planned improvements may include:

AI/LLM-based ticket classification
Automated priority and impact recommendations
Integration with ITSM platforms
Web-based operational dashboard
Ticket trend and incident analysis
Automated reporting and notifications

Author
Thein

Focus Areas:

Enterprise Application Support
AI-enabled IT Operations
Solution Architecture

GitHub:
https://github.com/theingit