import argparse
from report_reader import read_pmcf_report
from document_updater import update_documents
from self_trainer import train_ai

def main():
    parser = argparse.ArgumentParser(description="AI tool for managing medical documentation updates")
    parser.add_argument("pmcf_report", type=str, help="Path to the PMCF report")
    parser.add_argument("output_folder", type=str, help="Path to the output folder for updated documents")
    args = parser.parse_args()

    # Read the PMCF report
    conclusions = read_pmcf_report(args.pmcf_report)

    # Update the documents based on the report conclusions
    update_documents(conclusions, args.output_folder)

    # Train the AI with the new data
    train_ai(conclusions)

if __name__ == "__main__":
    main()
