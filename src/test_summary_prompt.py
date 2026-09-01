from prompt_builder import build_summary_prompt

ticket = {
    "Ticket ID": "INC-1001",
    "Priority": "High",
    "Application": "Payment System",
    "Description": "Users are unable to submit payment transactions. The application returns an error after clicking Submit."
}


prompt = build_summary_prompt(ticket)


print("AI Ticket Summary Prompt")
print("=" * 50)
print(prompt)
