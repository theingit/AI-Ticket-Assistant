"""
AI Ticket Assistant v0.1

Purpose:
- Read the tickets exported via ITSM.
- Print the ticket records.

Author: LN
"""
from pathlib import Path

#read the ticket file and returns its lines.
def read_ticket_file(ticket_file_path: Path):

    """Opens a file and returns its lines as a list."""    
    try:
        
        with open(ticket_file_path, "r", encoding="utf-8") as file:
            return file.readlines()            

    except FileNotFoundError:
        print(f"Error: The file '{ticket_file_path}' does not exist.")
        return None

def display_ticket_records(lines):  
    if lines is not None:
        for line in lines:
            print(line)

def main():   

    # Get the directory of the currently running script (src/)
    current_dir = Path(__file__).resolve().parent   

    # Go up one level to the project root, then into the data directory./
    ticket_file_path  = current_dir.parent / "data" / "tickets.csv"  
    
    # 1. Read the ticket file
    lines = read_ticket_file(ticket_file_path)
        
    if lines is None:
        return
    
    # 2. If file was found, print the header and display the ticket file contents.
    print("=" * 34)
    print(" AI Ticket Assistant v0.1")
    print("=" * 34)
    print()    
    
    display_ticket_records(lines)
      
                       
      
# Standard entry point to run the program
if __name__ == "__main__":
    main()