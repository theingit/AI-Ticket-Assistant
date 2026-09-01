# AI Ticket Assistant (Python)

A Python-based ITSM ticket analysis application for ticket validation, classification, impact analysis, prompt engineering, and AI-assisted ticket summarization.

## Overview

AI Ticket Assistant is a Python command-line application designed to support enterprise IT operations and application support activities.

The application can:

- Read tickets exported from an ITSM system
- Validate and parse ticket records
- Identify invalid ticket data and report validation errors
- Categorize valid tickets using rule-based classification
- Determine potential business impact
- Generate recommended actions
- Build structured prompts for AI processing
- Generate AI-assisted ticket summaries using a mock LLM provider for cost-free testing

The project demonstrates how traditional IT support automation can be combined with prompt engineering and an LLM-ready architecture.

## Key Features

- Ticket Import – Reads ticket records from CSV files
- Ticket Validation – Checks ticket data for missing or invalid values
- Validation Reporting – Aggregates valid and invalid records and reports individual validation errors
- Ticket Classification – Categorizes valid tickets using keyword-based business rules
- Impact Analysis – Determines potential operational impact based on ticket priority, application, and description
- Recommended Actions – Suggests appropriate actions based on potential impact
- Prompt Engineering – Builds structured prompts containing relevant ticket information and clear summarization requirements
- AI Summarization – Generates concise ticket summaries through an LLM-ready processing layer
- Mock LLM Provider – Provides cost-free testing of the AI processing pipeline without requiring paid API calls
- Operational Reporting – Generates ticket summaries, category summaries, impact summaries, critical-ticket lists, and detailed ticket information

## Technologies Used

- Python 3
- Visual Studio Code
- Git
- GitHub
- Python Standard Library (`csv`, `pathlib`, `collections`)
- Prompt Engineering
- LLM-ready application architecture

## Project Structure

```text
AI_Ticket_Assistant/ 
│ 
├── data/ 
│ └── tickets.csv 
│ 
├── src/ 
│ ├── read_tickets.py 
│ ├── prompt_builder.py 
│ ├── mock_llm.py 
│ ├── test_ai_pipeline.py 
│ ├── test_llm.py 
│ ├── test_mock_llm.py 
│ ├── test_prompt.py 
│ ├── test_summary_prompt.py 
│ └── test_ticket_summary.py 
│ 
├── .gitignore 
└── README.md
```

## How to Run
1. Clone the repository
git clone <your GitHub repository URL>

2. Move into the project directory
cd AI_Ticket_Assistant

3. Run the application
python src/read_tickets.py

The application reads the ticket data from the CSV file, validates the records, processes valid tickets, and generates the operational report with AI-assisted summaries.

## Sample Output
```text
==================================
 AI Ticket Assistant v1.0
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

--------------------------------
Ticket Details
--------------------------------
Ticket ID           : INC-1001
Priority            : High
Application         : Payment System
Category            : Payment Issue
Potential Impact    : Critical
Recommended Action  : Escalate immediately

AI Summary          :
Users are unable to complete payment transactions.
```
## AI Processing Architecture

The application separates ticket processing, prompt construction, and AI summarization into different components.

ITSM CSV Data
     ↓
Ticket Validation
     ↓
Valid Tickets
     ↓
Classification & Impact Analysis
     ↓
Prompt Builder
     ↓
AI / LLM Processing Layer
     ↓
AI Ticket Summary
     ↓
Operational Report

The current implementation uses a mock LLM provider to simulate AI responses without requiring paid API usage. The separation between prompt construction and the LLM processing layer allows a real LLM API to be integrated in the future without redesigning the core ticket-processing logic.

## Testing

The project includes test scripts covering:

- Ticket summary generation
- Prompt generation
- AI pipeline processing
- Mock LLM processing
- LLM library verification

The application was also tested using both valid and intentionally invalid CSV records to verify validation and aggregate error reporting.

Example validation result:

Total tickets imported : 20
Valid tickets          : 8
Invalid tickets        : 12

Invalid records include missing Priority, Application, or Description values and invalid Priority values such as Urgent.

## Future Improvements
Planned improvements may include:

- Integration with a real LLM API when an appropriate free or supported environment is available
- Structured JSON responses from the LLM
- AI-based ticket classification
- AI-assisted priority and impact recommendations
- Integration with ITSM platforms
- Web-based operational dashboard
- Ticket trend and incident analysis
- Automated reporting and notifications

## Author
Thein

Focus Areas:

Enterprise Application Support
AI-enabled IT Operations
Solution Architecture

GitHub:
https://github.com/theingit