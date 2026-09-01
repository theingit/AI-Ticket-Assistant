from mock_llm import generate_ticket_summary

ticket = {
    "Ticket ID": "INC-1002",
    "Priority": "Medium",
    "Application": "HR Portal",
    "Description": "User cannot download the monthly payslip from the HR portal."
}

summary = generate_ticket_summary(ticket)

print("AI Ticket Summary")
print("=" * 50)
print(summary)