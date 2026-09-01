def build_ticket_prompt(ticket):
    prompt = f"""
You are an IT support assistant.

Analyze the following IT support ticket.

Ticket ID: {ticket['Ticket ID']}
Priority: {ticket['Priority']}
Application: {ticket['Application']}
Description: {ticket['Description']}

Determine the most appropriate ticket category based on
the application and description.

Assess the potential business impact using the ticket
priority, application, number of affected users and described symptoms.

Recommend an appropriate support action based on the
potential impact.

Provide a concise and professional summary of the ticket.

Return the result in a clear and structured format.
"""

    return prompt

def build_summary_prompt(ticket):
    return f"""
You are an IT support assistant.


Summarize the following IT support ticket in one concise sentence.


Ticket ID: {ticket["Ticket ID"]}
Priority: {ticket["Priority"]}
Application: {ticket["Application"]}
Description: {ticket["Description"]}


Requirements:
- Summarize only the information provided.
- Do not invent additional details.
- Focus on the user's problem.
- Return one concise sentence.
"""
