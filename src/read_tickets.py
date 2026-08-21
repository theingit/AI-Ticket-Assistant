"""
AI Ticket Assistant v0.3

Purpose:
- Read the tickets exported via ITSM.
- Print the ticket records.


Author: Thein
"""
import csv
from pathlib import Path
from collections import Counter

# Define required column headers
REQUIRED_FIELDS = ["Ticket ID", "Priority", "Application", "Description"]
TICKET_PRIORITIES = ("High", "Medium", "Low")
CRITICAL_APPS = {"crm", "erp", "payment system", "production", "other"} 
#TICKET_CATEGORY = ("Payment Issue", "HR / Payroll", "Email Support", "OTHER")

# Read the ticket file, validate and return ticket records.
def validate_and_parse_csv(ticket_file_path: Path):

    """Opens a CSV file and returns ticket records as a list of dictionaries."""

    try:

        valid_tickets = [] #Declare an empty list to store all valid row records
        invalid_records_details = []
        total_imported = 0
        valid_count = 0
        invalid_count = 0
        #ticket_data = {field: [] for field in REQUIRED_FIELDS}        
        
        with open(ticket_file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            # 1. Validate Headers
            if not reader.fieldnames:
                print("Error: Invalid data. The CSV file is empty or missing headers.")
                return None

            missing_headers = [field for field in REQUIRED_FIELDS if field not in reader.fieldnames]
            
            if missing_headers:
                print(f"Error: Missing required column headers: {missing_headers}")
                return None

            # 2. Validate Row Data
            for row_number, row in enumerate(reader, start=2): # Headers are row 1
                total_imported += 1

                # Temporary dictionary to hold the cleaned data for the current row
                valid_ticket = {}
                row_errors = []
                is_row_valid = True

                for field in REQUIRED_FIELDS:
                    value = row.get(field)

                    # 1. Check if the field is missing from the row, or is just whitespace
                    if value is None or value.strip() == "":
                        is_row_valid = False
                        #print(f"Error: Missing value for '{field}' at row {row_number}")
                        error_message = f"Missing value for '{field}'"
                        row_errors.append(error_message)
                        #print(f"Error: {error_message} at row {row_number}")
                        continue  # Check remaining fields for more errors

                    clean_value = value.strip()

                     # 2. Specific Validation for Priority
                    if field == "Priority" and clean_value not in TICKET_PRIORITIES:
                        is_row_valid = False
                        error_message = (f"Invalid Priority '{clean_value}'. "f"Must be High, Medium, or Low.")
                        row_errors.append(error_message)
                        #print(f"Error: {error_message} at row {row_number}")
                        #print(f"Error: Invalid Priority '{clean_value}' at row {row_number}. Must be High, Medium, or Low.")
                        continue                    
                
                    valid_ticket[field] = clean_value

                #valid_tickets.append(valid_ticket)
                # --- TRACK AND COUNT RECODS ---
                if is_row_valid:
                    valid_count += 1
                    valid_tickets.append(valid_ticket)
                else:
                    invalid_count += 1
                    invalid_records_details.append({
                        "row_number": row_number,
                        "errors": row_errors,
                        "raw_data": row
                    })
                
        # Print operational metrics summary
        print("\nTicket Import Summary ")
        print("--------------------------------")
        print(f"Total tickets imported : {total_imported}")
        print(f"Valid tickets          : {valid_count}")
        print(f"Invalid tickets        : {invalid_count}")
        print("--------------------------------")

        # Print structural details about errors
        if invalid_records_details:
            print("\n--- Invalid Records Details ---")
            for record in invalid_records_details:
                errors_str = " | ".join(record["errors"])
                print(f"Row {record['row_number']}: {errors_str}")
                print(f"   Data: {record['raw_data']}\n")


        # Return everything so your main program can use the data and logs    
        return valid_tickets, invalid_records_details, total_imported, valid_count, invalid_count
        
    except FileNotFoundError:
        print(f"Error: The file '{ticket_file_path}' does not exist.")
        return None

def categorize_ticket(description):

    desc_lower = description.lower()

    # Check for Payment Issue
    if any(keyword in desc_lower for keyword in ("payment", "transaction", "submit")):    
        return "Payment Issue"

    elif any(keyword in desc_lower for keyword in ("erp", "orders")):    
        return "ERP System Issue"

    elif any(keyword in desc_lower for keyword in ("data", "database", "sql", "connection", "timeout")):    
        return "Database"

    # Check for HR / Payroll system issues    
    elif any(keyword in desc_lower for keyword in ("payslip", "salary", "hr")):    
        return "HR / Payroll"

    # Check for Email Support 
    elif any(keyword in desc_lower for keyword in ("email", "signature", "mail")):    
        return "Email Support"
         
    # Check for Network issues
    elif any(keyword in desc_lower for keyword in ("wifi", "vpn", "internet slow")):
        return "Network"

    # Check for Access & Security issues
    elif any(keyword in desc_lower for keyword in ("password", "login", "reset", "access denied")):
    #elif "password" in desc_lower or "login" in desc_lower or "access denied" in desc_lower:
        return "Access & Security"
        
    # Check for Hardware issues
    elif any(keyword in desc_lower for keyword in ("monitor", "printer", "laptop", "computer")):
        return "Hardware"
        
    # Check for Software/Application errors
    elif any(keyword in desc_lower for keyword in ("crash", "bug", "error code")):
        return "Software Error"   
        
    # Default category if no keywords match
    else:
        return "General Inquiry"    

def determine_potential_impact(priority, application, description):
    desc_lower = description.lower()

    # 1. CRITICAL IMPACT: High priority on core business systems or major outages
    #critical_apps = {"crm", "erp", "payment system", "production"} #must be small letter bcoz desc.lower()
    is_core_app = application.lower() in CRITICAL_APPS
    is_outage = "multiple users" in desc_lower or "down" in desc_lower or "outage" in desc_lower or "crash" in desc_lower or "connection" in desc_lower or "timeout" in desc_lower or "database" in desc_lower
    
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

def generate_ticket_summary(tickets):
                         
    priorities = [ticket["Priority"] for ticket in tickets]
    priority_counts = Counter(priorities)
    total_tickets = len(tickets)
    
    print("\nValid Ticket Summary")
    print("--------------------------------")
    print(f"Total Tickets : {total_tickets}")
    print(f"High Priority : {priority_counts['High']}")
    print(f"Medium        : {priority_counts['Medium']}")
    print(f"Low           : {priority_counts['Low']}")  
    print(f"--------------------------------\n")  
    
def generate_ticket_category_summary(tickets):
    categories = [ticket["Category"] for ticket in tickets]
    category_counts = Counter(categories)

    print("Category Summary of Valid Tickets")
    print("--------------------------------")  
    """    
    for item, count in category_counts.items():
        if count > 0:    
            print(f"{item:<20}: {count}")
    """
    #alternative way. filter if any duplicate
    filtered_counts = {item: count for item, count in category_counts.items() if count > 0}
    for item, count in filtered_counts.items():
        print(f"{item}: {count}")  
    
    print(f"--------------------------------\n") 

def generate_impact_summary(tickets):
    impacts = [ticket["Potential Impact"] for ticket in tickets]
    impact_counts = Counter(impacts)

    print("Impact Summary of Valid Tickets")
    print("--------------------------------")  
    for item, count in impact_counts.items():
        if count > 0:    
            print(f"{item:<10}: {count}")
            
    print(f"--------------------------------\n") 

def print_critical_issues(tickets):
    critical_issues = [item for item in tickets if item.get("Potential Impact") == "Critical"]

    print("Tickets Requiring Attention")
    print("--------------------------------")     
    #print(critical_issues)
    for issue in critical_issues:
        print(f"{issue['Ticket ID']} - {issue['Potential Impact']} - {issue['Category']}\n")  
    print("--------------------------------")     

def generate_reports(tickets):

    # 1. Print the ticket summary 
    generate_ticket_summary(tickets)     

    # Categorize tickets, determine potential impact, and display the analysis.
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

        ticket["Recommended Action"] = Recommended_action(impact=ticket["Potential Impact"])
        
        
    # 2. Print the ticket category summary
    generate_ticket_category_summary(tickets)

    # 3. Print the impact summary
    generate_impact_summary(tickets)

    # 4. Extract Critical Tickets Requiring Attention
    print_critical_issues(tickets)

    # 5. Print all ticket details
    print("Ticket Details")  
    print("--------------------------------")   
    for ticket in tickets:                 
        print(f"{'Ticket ID':<20}: {ticket['Ticket ID']}")    
        print(f"{'Priority':<20}: {ticket['Priority']}")    
        print(f"{'Application':<20}: {ticket['Application']}")          
        print(f"{'Category':<20}: {ticket['Category']}")
        print(f"{'Potential Impact':<20}: {ticket['Potential Impact']}")
        print(f"{'Recommended Action':<20}: {ticket['Recommended Action']}")
        print()
        print(f"{'Description':<20}:\n{ticket['Description']}")  
        print()
         
def Recommended_action(impact):
    desc_impact = impact.lower()

    if desc_impact == "critical":
        return "Escalate immediately"

    elif desc_impact == "high":
        return "Prioritize for investigation"

    elif desc_impact == "medium":
        return "Investigate within normal SLA"

    else:
        return "Handle as standard service request"
    
def main():   

    # Get the directory of the currently running script (src/)
    current_dir = Path(__file__).resolve().parent   

    # Go up one level to the project root, then into the data directory./
    ticket_file_path  = current_dir.parent / "data" / "tickets.csv"     
 
    
    # 1. Display the header.
    print("=" * 34)
    print(" AI Ticket Assistant v0.3")
    print("=" * 34)
    print()  

    # 2. Read, validate and parse the ticket data.
    result = validate_and_parse_csv(ticket_file_path)
           
    if result is None:
        print("Import failed immediately due to header or structural file errors.")
        return

    # Unpack the tuple into local main variables
    valid_tickets, invalid_details, total, valid_qty, invalid_qty = result

    # 3. generate report
    generate_reports(valid_tickets)
                   
      
# Standard entry point to run the program
if __name__ == "__main__":
    main()