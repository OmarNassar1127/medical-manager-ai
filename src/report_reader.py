import json
from docx import Document
from session_memory import SessionMemory

def read_pmcf_report(report_path, session_memory: SessionMemory):
    """
    Reads the PMCF report and extracts relevant conclusions.
    
    Args:
        report_path (str): Path to the PMCF report file.
        session_memory (SessionMemory): Instance of SessionMemory to log interactions.
    
    Returns:
        dict: Extracted conclusions from the report.
    """
    session_memory.add_interaction({"action": "read_pmcf_report", "input": report_path})
    
    if report_path.endswith('.json'):
        with open(report_path, 'r') as file:
            report_data = json.load(file)
        conclusions = report_data.get('conclusions', {})
    elif report_path.endswith('.docx'):
        document = Document(report_path)
        report_text = "\n".join([para.text for para in document.paragraphs])
        # Placeholder for actual extraction logic from DOCX text
        conclusions = {"conclusions": report_text}
    else:
        raise ValueError("Unsupported file format. Please provide a .json or .docx file.")
    
    session_memory.add_interaction({"action": "read_pmcf_report", "output": conclusions})
    
    return conclusions
