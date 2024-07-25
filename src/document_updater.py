import os
import shutil
import logging
import time  # Import the time module
from datetime import datetime
from docx import Document
from session_memory import SessionMemory

def update_documents(conclusions, output_folder, session_memory):
    """
    Updates the documents based on the extracted conclusions.

    Args:
        conclusions (dict): Extracted conclusions from the PMCF report.
        output_folder (str): Path to the output folder for updated documents.
        session_memory (SessionMemory): Instance of SessionMemory to track interactions.

    Raises:
        NotADirectoryError: If the output_folder is not a directory.
    """
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    if not os.path.isdir(output_folder):
        logging.error(f"Error: {output_folder} is not a directory")
        raise NotADirectoryError(f"{output_folder} is not a directory")

    try:
        # Create a new folder for the updated documents
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            logging.info(f"Created output folder: {output_folder}")
        session_memory.add_interaction({"action": "create_output_folder", "folder": output_folder})
    except OSError as e:
        logging.error(f"Error creating output folder: {e}")
        raise

    try:
        # Check if previous_versions folder exists, create if it doesn't
        previous_versions_folder = "previous_versions"
        if not os.path.exists(previous_versions_folder):
            os.makedirs(previous_versions_folder)
            logging.info(f"Created previous versions folder: {previous_versions_folder}")

        # Copy previous versions of documents to the new folder
        for filename in os.listdir(previous_versions_folder):
            src = os.path.join(previous_versions_folder, filename)
            dst = os.path.join(output_folder, filename)
            shutil.copy(src, dst)
            logging.info(f"Copied file: {src} to {dst}")
        session_memory.add_interaction({"action": "copy_previous_versions", "source": previous_versions_folder, "destination": output_folder})
    except (OSError, shutil.Error) as e:
        logging.error(f"Error handling previous versions: {e}")
        raise

    try:
        # Update document content
        for filename in os.listdir(output_folder):
            file_path = os.path.join(output_folder, filename)
            update_document_content(file_path, conclusions, session_memory)
            time.sleep(2)  # Add a delay after updating the file

        session_memory.add_interaction({"action": "update_documents", "updated_files": os.listdir(output_folder)})
    except OSError as e:
        logging.error(f"Error updating documents: {e}")
        raise

    try:
        # Update version numbers in file names after content update
        for filename in os.listdir(output_folder):
            old_path = os.path.join(output_folder, filename)
            new_filename = update_version_number(filename)
            new_path = os.path.join(output_folder, new_filename)
            os.rename(old_path, new_path)
            logging.info(f"Renamed file: {old_path} to {new_path}")
    except OSError as e:
        logging.error(f"Error renaming documents: {e}")
        raise

    try:
        # Create a readme.txt with sections that need to be changed
        create_readme(output_folder, conclusions)
        session_memory.add_interaction({"action": "create_readme", "file": os.path.join(output_folder, "readme.txt")})
    except IOError as e:
        logging.error(f"Error creating readme file: {e}")
        raise

    logging.info("Document update process completed successfully")

def update_version_number(filename):
    """
    Updates the version number in the file name.

    Args:
        filename (str): Original file name.

    Returns:
        str: Updated file name with incremented version number.
    """
    name, ext = os.path.splitext(filename)
    if "_v" in name:
        base_name, version = name.rsplit("_v", 1)
        new_version = int(version) + 1
        new_filename = f"{base_name}_v{new_version}{ext}"
    else:
        new_filename = f"{name}_v1{ext}"

    return new_filename

def update_document_content(filepath, conclusions, session_memory):
    """
    Updates the content of the document based on the extracted conclusions.

    Args:
        filepath (str): Path to the document file.
        conclusions (dict): Extracted conclusions from the PMCF report.
        session_memory (SessionMemory): Instance of SessionMemory to track interactions.
    """
    logging.info(f"Attempting to update document content in {filepath}")
    logging.info(f"Current directory: {os.getcwd()}")
    logging.info(f"File exists: {os.path.exists(filepath)}")
    logging.info(f"File size: {os.path.getsize(filepath) if os.path.exists(filepath) else 'N/A'}")
    logging.info(f"Directory contents: {os.listdir(os.path.dirname(filepath))}")

    try:
        doc = Document(filepath)
        for paragraph in doc.paragraphs:
            for key, value in conclusions.items():
                if key in paragraph.text:
                    paragraph.text = paragraph.text.replace(key, value)
                    logging.info(f"Updated content in {filepath}: replaced '{key}' with '{value}'")
        doc.save(filepath)
        logging.info(f"Saved updated document: {filepath}")
        session_memory.add_interaction({"action": "update_document_content", "file": filepath, "updates": list(conclusions.keys())})
    except Exception as e:
        logging.error(f"Error updating document content in {filepath}: {e}")
        raise

def create_readme(output_folder, conclusions):
    """
    Creates a readme.txt with sections that need to be changed.

    Args:
        output_folder (str): Path to the output folder for updated documents.
        conclusions (dict): Extracted conclusions from the PMCF report.
    """
    readme_path = os.path.join(output_folder, "readme.txt")
    try:
        with open(readme_path, 'w') as readme_file:
            readme_file.write("Sections that need to be changed:\n")
            for key, value in conclusions.items():
                readme_file.write(f"{key}: {value}\n")
        logging.info(f"Created readme file: {readme_path}")
    except IOError as e:
        logging.error(f"Error writing to readme file: {e}")
        raise
