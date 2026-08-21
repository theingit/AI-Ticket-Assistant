# AI Ticket Assistant (Python)

A Python-based ITSM ticket analysis application for ticket validation, classification, impact analysis, and operational reporting.

## Overview

AI Ticket Assistant is a Python command-line application designed to support IT operations and application support activities.

The application can:

- Read tickets exported from an ITSM system
- Validate and parse ticket records
- Identify invalid ticket data and report validation errors
- Categorize valid tickets using rule-based classification
- Determine potential business impact
- Generate recommended actions
- Generate operational summaries and ticket reports

This project simulates real-world operational support tasks performed by Application Support Engineers and Production Support Engineers.

## Key Features

- **Ticket Import** – Reads ticket records from CSV files
- **Ticket Validation** – Checks ticket data for missing or invalid values
- **Validation Reporting** – Aggregates valid and invalid records and reports individual validation errors
- **Ticket Classification** – Categorizes valid tickets using keyword-based business rules
- **Impact Analysis** – Determines potential operational impact based on ticket priority, application, and description
- **Recommended Actions** – Suggests an appropriate action based on priority and potential impact
- **Operational Reporting** – Generates ticket summaries, category summaries, impact summaries, and tickets requiring attention

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
```

## How to Run
1. Clone the repository
git clone https://github.com/theingit/AI-Ticket-Assistant.git

2. Move into the project directory
cd AI_Ticket_Assistant

3. Run the application
python src/read_tickets.py

## Sample Output
==================================
 AI Ticket Assistant v0.3
==================================

Ticket Import Summary
--------------------------------
Total tickets imported : 20
Valid tickets          : 8
Invalid tickets        : 12
--------------------------------

--- Invalid Records Details ---
Row 8: Missing value for 'Priority'

Row 9: Invalid Priority 'Urgent'. Must be High, Medium, or Low.

Row 12: Missing value for 'Priority' | Missing value for 'Description'

Row 15: Missing value for 'Priority' | Missing value for 'Application' | Missing value for 'Description'

--------------------------------
Valid Ticket Summary
--------------------------------
Total Tickets : 8
High Priority : 2
Medium        : 3
Low           : 3
--------------------------------

Category Summary of Valid Tickets
--------------------------------
Payment Issue: 1
HR / Payroll: 2
Email Support: 2
ERP System Issue: 1
Database: 1
Access & Security: 1
--------------------------------

Impact Summary of Valid Tickets
--------------------------------
Critical : 2
High     : 1
Medium   : 2
Low      : 3
--------------------------------

Tickets Requiring Attention
--------------------------------
INC-1001 - Critical - Payment Issue
INC-1005 - Critical - Database

## Future Improvements
Planned improvements may include:

LLM-based ticket summarization and analysis
Prompt engineering and structured AI responses
Automated priority and impact recommendations
Integration with ITSM platforms
Web-based operational dashboard
Ticket trend and incident analysis
Automated reporting and notifications

## Author
Thein

Focus Areas:

Enterprise Application Support
AI-enabled IT Operations
Solution Architecture

GitHub:
https://github.com/theingit