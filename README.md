# Medical Manager AI

Medical Manager AI is an AI-powered tool designed to read PMCF (Post-Market Clinical Follow-up) reports and generate updated versions of existing medical documents. It updates statements associated with pertinent risks and document version details, such as dates, numbers, and summaries of changes.

## Features

- Reads and analyzes PMCF reports
- Updates existing medical documents based on new information
- Self-training capability to improve performance over time
- RAG (Red, Amber, Green) status system for flagging sections with low confidence

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

## Usage

1. Prepare your PMCF report in JSON format. Ensure that the report includes a `conclusions` section.

2. Run the tool with the following command:
   ```bash
   python src/main.py <path_to_pmcf_report> <output_folder>
   ```
   Replace `<path_to_pmcf_report>` with the path to your PMCF report file and `<output_folder>` with the path to the folder where you want the updated documents to be saved.

## Model Setup and Training

The AI model uses the Hugging Face Transformers library. To set up and train the model:

1. Ensure you have installed all dependencies from `requirements.txt`.

2. Prepare your training data:
   - Create a directory named `training_data` in the project root.
   - Add your PMCF reports and corresponding updated documents to this directory.

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
