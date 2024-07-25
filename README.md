# medical-manager-ai

## Introduction
The `medical-manager-ai` tool is designed to read PMCF reports and generate drafts of updated versions of existing documents. It updates statements associated with pertinent risks and document version details such as dates, numbers, summaries of changes, etc. The tool also has a self-training capability to improve its performance over time.

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
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To use the `medical-manager-ai` tool, follow these steps:

1. Prepare your PMCF report in JSON format. Ensure that the report includes a `conclusions` section.

2. Run the tool with the following command:
    ```bash
    python src/main.py <path_to_pmcf_report> <output_folder>
    ```
    Replace `<path_to_pmcf_report>` with the path to your PMCF report file and `<output_folder>` with the path to the folder where you want the updated documents to be saved.

## Contributing
We welcome contributions to the `medical-manager-ai` project! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
    ```bash
    git checkout -b your-feature-branch
    ```
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
    ```bash
    git push origin your-feature-branch
    ```
5. Create a pull request to the main repository.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For support or inquiries, please contact Omar Nassar at [your-email@example.com].
