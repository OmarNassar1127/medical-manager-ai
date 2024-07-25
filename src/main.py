import argparse
import time  # Import the time module
from report_reader import read_pmcf_report
from document_updater import update_documents
from self_trainer import train_ai
from session_memory import SessionMemory  # Import the SessionMemory class
from file_picker import file_picker  # Import the file_picker function

def main():
    session_memory = SessionMemory()  # Instantiate SessionMemory

    print("Hello! What can I help you with today?")
    print("1. Process a PMCF report")
    print("2. Exit")
    choice = input("Please enter the number of your choice: ")

    if choice == "1":
        print("Please select the PMCF report file:")
        pmcf_report_path = file_picker()
        if not pmcf_report_path:
            print("No file selected. Exiting.")
            return

        print("Please select the output folder for updated documents:")
        output_folder_path = file_picker()
        if not output_folder_path:
            print("No folder selected. Exiting.")
            return

        # Read the PMCF report
        conclusions = read_pmcf_report(pmcf_report_path, session_memory)
        session_memory.add_interaction({"action": "read_pmcf_report", "data": conclusions})  # Add interaction to session memory

        # Add a short delay before updating documents
        time.sleep(2)

        # Update the documents based on the report conclusions
        update_documents(conclusions, output_folder_path, session_memory)
        session_memory.add_interaction({"action": "update_documents", "data": output_folder_path})  # Add interaction to session memory

        # Add a short delay before training the AI
        time.sleep(2)

        # Train the AI with the new data
        train_ai(conclusions, session_memory)
        session_memory.add_interaction({"action": "train_ai", "data": None})  # Add interaction to session memory

        print("The documents have been updated and the AI has been trained with the new data.")
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice. Please restart the program and try again.")

if __name__ == "__main__":
    main()
