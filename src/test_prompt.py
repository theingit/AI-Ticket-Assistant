from prompt_builder import build_ticket_prompt

ticket = {
    "Ticket ID": "INC-1001",
    "Priority": "High",
    "Application": "Payment System",
    "Description": "Users are unable to submit payment transactions. The application returns an error after clicking Submit."
}

prompt = build_ticket_prompt(ticket)

print("Generated AI Prompt")
print("=" * 50)
print(prompt)