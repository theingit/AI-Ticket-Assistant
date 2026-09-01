from prompt_builder import build_ticket_prompt
from prompt_builder import build_summary_prompt
from mock_llm import generate_ai_response
from mock_llm import generate_ai_summary

ticket = {
    "Ticket ID": "INC-1030",
    "Priority": "Medium",
    "Application": "CRM",
    "Description": "Users are unable to export the monthly report."
}


#prompt = build_ticket_prompt(ticket)
#response = generate_ai_response(prompt)

prompt = build_summary_prompt(ticket)
summary = generate_ai_summary(ticket) #call openai api

print("AI Ticket Processing")
print("=" * 50)


print("\nGenerated Prompt")
print("-" * 50)
print(prompt)


print("\nAI Response")
print("-" * 50)
print(summary) #print(response)
