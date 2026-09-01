def generate_ai_response(prompt):
    return """
Category: Payment Issue
Potential Impact: Critical
Recommended Action: Escalate immediately
Summary: Users are unable to submit payment transactions.
"""

def generate_ai_summary(prompt):#def generate_ai_summary(ticket):
    #description = ticket["Description"].lower()
    #print("DEBUG prompt type:", type(prompt))
    prompt_lower = prompt.lower()

    if "payment" in prompt_lower:
        return "Users are unable to complete payment transactions."

    if "timeout" in prompt_lower or "database" in prompt_lower:
            return "Users are encountering connection timeout issue."

    if "payslip" in prompt_lower:
        return "The user is unable to access or download their payslip."


    if "login" in prompt_lower:
        return "Users are unable to log in to the application."


    if "email" in prompt_lower:
        return "The user is experiencing an email-related issue."
    
    return "The ticket describes an IT-related issue requiring investigation."

    
