import argparse
import time  # Import the time module
from report_reader import read_pmcf_report
from document_updater import update_documents
from self_trainer import train_ai
from session_memory import SessionMemory  # Import the SessionMemory class

def main():
    session_memory = SessionMemory()  # Instantiate SessionMemory

    parser = argparse.ArgumentParser(description="AI tool for managing medical documentation updates")
    parser.add_argument("pmcf_report", type=str, help="Path to the PMCF report")
    parser.add_argument("output_folder", type=str, help="Path to the output folder for updated documents")
    args = parser.parse_args()

    # Read the PMCF report
    conclusions = read_pmcf_report(args.pmcf_report, session_memory)
    session_memory.add_interaction({"action": "read_pmcf_report", "data": conclusions})  # Add interaction to session memory

    # Add a short delay before updating documents
    time.sleep(2)

    # Update the documents based on the report conclusions
    update_documents(conclusions, args.output_folder, session_memory)
    session_memory.add_interaction({"action": "update_documents", "data": args.output_folder})  # Add interaction to session memory

    # Add a short delay before training the AI
    time.sleep(2)

    # Train the AI with the new data
    train_ai(conclusions, session_memory)
    session_memory.add_interaction({"action": "train_ai", "data": None})  # Add interaction to session memory

if __name__ == "__main__":
    main()
