from mock_llm import generate_ai_response

prompt = """
You are an IT support assistant.


Analyze the following IT support ticket.


Ticket ID: INC-1001
Priority: High
Application: Payment System
Description: Users are unable to submit payment transactions.
"""


response = generate_ai_response(prompt)


print("Mock AI Response")
print("=" * 50)
print(response)
