"""
AI Ticket Assistant v0.1

Purpose:
- Read the tickets exported via ITSM.
- Print the ticket records.

Author: LN
"""
import csv
from pathlib import Path


# Read the ticket file and return ticket records.
def read_ticket_file(ticket_file_path: Path):

    """Opens a CSV file and returns ticket records as a list of dictionaries."""

    try:
        
        with open(ticket_file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)            

    except FileNotFoundError:
        print(f"Error: The file '{ticket_file_path}' does not exist.")
        return None


def main():   

    # Get the directory of the currently running script (src/)
    current_dir = Path(__file__).resolve().parent   

    # Go up one level to the project root, then into the data directory./
    ticket_file_path  = current_dir.parent / "data" / "tickets.csv"  
    
    # 1. Read and parse the ticket data.
    tickets = read_ticket_file(ticket_file_path)
        
    if tickets is None:
        return
    
    # 2. Display the ticket records.
    print("=" * 34)
    print(" AI Ticket Assistant v0.1")
    print("=" * 34)
    print()  

    # 3. display the ticket data
    for ticket in tickets:
        print(ticket["Ticket ID"])
        print(ticket["Priority"])
        print(ticket["Application"])
        print(ticket["Description"])
                   
      
# Standard entry point to run the program
if __name__ == "__main__":
    main()