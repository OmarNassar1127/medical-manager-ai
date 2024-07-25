# Medical Manager AI

Medical Manager AI is an AI-powered tool designed to read PMCF (Post-Market Clinical Follow-up) reports and generate updated versions of existing medical documents. It updates statements associated with pertinent risks and document version details, such as dates, numbers, and summaries of changes.

## Features

- Reads and analyzes PMCF reports in both JSON and DOCX formats
- Updates existing medical documents based on new information
- Self-training capability to improve performance over time
- RAG (Red, Amber, Green) status system for flagging sections with low confidence
- Conversational AI interaction for user-friendly experience

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/OmarNassar1127/medical-manager-ai.git
   cd medical-manager-ai
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Interacting with the AI

The Medical Manager AI now supports a conversational interface and can process DOCX files directly for PMCF reports. Here's how to interact with the AI:

1. **Start the AI Tool:**
   Run the `main.py` script to start the AI tool:
   ```bash
   python src/main.py
   ```

2. **Greet the AI:**
   The AI will greet you with: "Hello! What can I help you with today?"

3. **Choose an Action:**
   The AI will provide you with options:
   - **Option 1:** Process a PMCF report
   - **Option 2:** Exit
   Enter the number corresponding to your choice.

4. **Provide the PMCF Report:**
   If you choose to process a PMCF report, the AI will ask for the file path:
   ```plaintext
   Please provide the path to the PMCF report: [your_pmcf_report_path]
   ```
   You can now provide the path to either a JSON or DOCX file.

5. **Specify Output Folder:**
   Next, provide the path for the output folder:
   ```plaintext
   Please provide the path to the output folder for updated documents: [your_output_folder_path]
   ```

6. **AI Processing:**
   The AI will process the PMCF report, update the documents, and train itself. You'll be notified once complete:
   ```plaintext
   The documents have been updated and the AI has been trained with the new data.
   ```

7. **Exit:**
   If you choose to exit, the AI will say goodbye and terminate the program.

## Model Setup and Training

The AI model uses the Hugging Face Transformers library. To set up and train the model:

1. Ensure you have installed all dependencies from `requirements.txt`.

2. Prepare your training data:
   - Create a directory named `training_data` in the project root.
   - Add your PMCF reports (JSON or DOCX) and corresponding updated documents to this directory.

3. Run the training script:
   ```bash
   python src/train_model.py --data_dir training_data/ --output_dir trained_model/
   ```

4. The trained model will be saved in the specified output directory.

## Self-Training

The tool includes a self-training mechanism to improve its performance over time:

1. After processing a batch of PMCF reports, run:
   ```bash
   python src/self_train.py --new_data path/to/processed_reports/
   ```

2. The model will update itself based on the new data.

## RAG Status System

The tool uses a RAG (Red, Amber, Green) status system to flag sections with low confidence:

- Red: Low confidence, requires manual review
- Amber: Medium confidence, may require review
- Green: High confidence, likely accurate

Review the RAG status in the output logs to identify areas that may need human attention.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For support or inquiries, please contact Omar Nassar at [your-email@example.com].
