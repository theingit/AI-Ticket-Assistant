"""
AI Ticket Assistant v0.1

Purpose:
- Read the tickets exported via ITSM.
- Print the ticket records.

Todo:
Split fun: Read CSV read_tickets(), Parse CSV parse_tickets(), Validate data validate_ticket()

Author: LN
"""
import csv
from pathlib import Path
# Define required column headers
REQUIRED_FIELDS = ["Ticket ID", "Priority", "Application", "Description"]
TICKET_PRIORITIES = ("High", "Medium", "Low")
#TICKET_CATEGORY = ("Payment Issue", "HR / Payroll", "Email Support", "OTHER")

# Read the ticket file, validate and return ticket records.
def validate_and_parse_csv(ticket_file_path: Path):

    """Opens a CSV file and returns ticket records as a list of dictionaries."""

    try:

        valid_tickets = [] #Declare an empty list to store all valid row records
        #ticket_data = {field: [] for field in REQUIRED_FIELDS}        
        
        with open(ticket_file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            # 1. Validate Headers
            if not reader.fieldnames:
                print("Error: Invalid data. The CSV file is empty or missing headers.")
                return None

            missing_headers = [
                field for field in REQUIRED_FIELDS 
                if field not in reader.fieldnames
                ]
            
            if missing_headers:
                print(f"Error: Missing required column headers: {missing_headers}")
                return None

            # 2. Validate Row Data
            for row_number, row in enumerate(reader, start=2): # Headers are row 1
                # Temporary dictionary to hold the cleaned data for the current row
                valid_ticket = {}

                for field in REQUIRED_FIELDS:
                    value = row.get(field)

                    # 1. Check if the field is missing from the row, or is just whitespace
                    if value is None or value.strip() == "":
                        print(f"Error: Missing value for '{field}' at row {row_number}")
                        return None

                    clean_value = value.strip()

                     # 2. Specific Validation for Priority
                    if field == "Priority" and clean_value not in TICKET_PRIORITIES:
                        print(f"Error: Invalid Priority '{clean_value}' at row {row_number}. Must be High, Medium, or Low.")
                        return None                    
                
                    valid_ticket[field] = clean_value

                valid_tickets.append(valid_ticket)
                    

        print("All CSV data validations passed!\n")             
        return valid_tickets
       

    except FileNotFoundError:
        print(f"Error: The file '{ticket_file_path}' does not exist.")
        return None

def categorize_ticket(description):

    desc_lower = description.lower()

    # 1. Check for Payment Issue
    if any(keyword in desc_lower for keyword in ("payment", "transaction", "submit")):    
        return "Payment Issue"

    # 2. Check for HR / Payroll system issues    
    elif any(keyword in desc_lower for keyword in ("payslip", "salary", "hr")):    
        return "HR / Payroll"

    # 3. Check for Email Support 
    elif any(keyword in desc_lower for keyword in ("email", "signature", "mail")):    
        return "Email Support"

    # 4. Check for Access & Security issues
    elif any(keyword in desc_lower for keyword in ("password", "login", "reset", "access denied")):
    #elif "password" in desc_lower or "login" in desc_lower or "access denied" in desc_lower:
        return "Access & Security"
        
    # 5. Check for Hardware issues
    elif any(keyword in desc_lower for keyword in ("monitor", "printer", "laptop", "computer")):
        return "Hardware"
        
    # 6. Check for Software/Application errors
    elif any(keyword in desc_lower for keyword in ("crash", "bug", "error code")):
        return "Software Error"
        
    # 7. Check for Network issues
    elif any(keyword in desc_lower for keyword in ("wifi", "vpn", "internet slow")):
        return "Network"
        
    # 8. Default category if no keywords match
    else:
        return "General Inquiry"    

def determine_potential_impact(priority, application, description):
    desc_lower = description.lower()

    # 1. CRITICAL IMPACT: High priority on core business systems or major outages
    critical_apps = {"crm", "erp", "payment system", "production"} #must be small letter bcoz desc.lower()
    is_core_app = application.lower() in critical_apps
    is_outage = "multiple users" in desc_lower or "down" in desc_lower or "outage" in desc_lower or "crash" in desc_lower
    
    if priority == "High" and (is_core_app or is_outage):
        return "Critical"
        
    # 2. HIGH IMPACT: High priority general tasks OR Medium priority on core systems
    elif priority == "High" or (priority == "Medium" and is_core_app):
        return "High"
        
    # 3. MEDIUM IMPACT: Medium priority general tasks OR Low priority security issues
    elif priority == "Medium" or "security" in desc_lower or "password" in desc_lower:
        return "Medium"
        
    # 4. LOW IMPACT: Low priority non-core systems
    else:
        return "Low"

def main():   

    # Get the directory of the currently running script (src/)
    current_dir = Path(__file__).resolve().parent   

    # Go up one level to the project root, then into the data directory./
    ticket_file_path  = current_dir.parent / "data" / "tickets.csv"     
 
    
    # 1. Display the header.
    print("=" * 34)
    print(" AI Ticket Assistant v0.1")
    print("=" * 34)
    print()  

    # 2. Read, validate and parse the ticket data.
    tickets = validate_and_parse_csv(ticket_file_path)
           
    if tickets is None:
        return
    
    # 3. Categorize tickets, determine potential impact, and display the analysis.
    for ticket in tickets:
        #print(ticket) #print(ticket) prints data as dictionary    
        
        #Call categorize_ticket to categorize the ticket.
        ticket["Category"] = categorize_ticket(ticket["Description"])

        #Call determine_potential_impact to determine the impact
        ticket["Potential Impact"] = determine_potential_impact(
            priority=ticket["Priority"],
            application=ticket["Application"],
            description=ticket["Description"]        
        )
        
        # Display the enhanced ticket information.
        print(f"{'Ticket ID':<12}: {ticket['Ticket ID']}")    
        print(f"{'Priority':<12}: {ticket['Priority']}")    
        print(f"{'Application':<12}: {ticket['Application']}")  
        print(f"{'Description':<12}: {ticket['Description']}")  
        print(f"{'Category':<12}: {ticket['Category']}")
        print(f"{'Potential Impact':<12}: {ticket['Potential Impact']}")
        print()
                   
      
# Standard entry point to run the program
if __name__ == "__main__":
    main()