import json
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
    
    with open(report_path, 'r') as file:
        report_data = json.load(file)
    
    # Extract conclusions from the report data
    conclusions = report_data.get('conclusions', {})
    
    session_memory.add_interaction({"action": "read_pmcf_report", "output": conclusions})
    
    return conclusions
