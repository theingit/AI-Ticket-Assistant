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

#def validate_ticket(ticket):
    #validate required fields, priority, identify invalid tickets, keep valid and invalid data distinguishable
    #return whether the ticket is valid and, eventually, an explanation of what's wrong.

    #return


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
    
    # 3. display the ticket data
    for ticket in tickets:
        #print(ticket) #print as dictionary        
        print(f"{'Ticket ID':<12}: {ticket['Ticket ID']}")    
        print(f"{'Priority':<12}: {ticket['Priority']}")    
        print(f"{'Application':<12}: {ticket['Application']}")  
        print(f"{'Description':<12}: {ticket['Description']}")  
        print()
                   
      
# Standard entry point to run the program
if __name__ == "__main__":
    main()