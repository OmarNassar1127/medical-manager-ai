import os
import shutil
from datetime import datetime
from docx import Document

def update_documents(conclusions, output_folder):
    """
    Updates the documents based on the extracted conclusions.
    
    Args:
        conclusions (dict): Extracted conclusions from the PMCF report.
        output_folder (str): Path to the output folder for updated documents.
    """
    # Create a new folder for the updated documents
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Copy previous versions of documents to the new folder
    previous_versions_folder = "previous_versions"
    for filename in os.listdir(previous_versions_folder):
        shutil.copy(os.path.join(previous_versions_folder, filename), output_folder)
    
    # Update version numbers in file names and document content
    for filename in os.listdir(output_folder):
        new_filename = update_version_number(filename)
        os.rename(os.path.join(output_folder, filename), os.path.join(output_folder, new_filename))
        update_document_content(os.path.join(output_folder, new_filename), conclusions)
    
    # Create a readme.txt with sections that need to be changed
    create_readme(output_folder, conclusions)

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

def update_document_content(filepath, conclusions):
    """
    Updates the content of the document based on the extracted conclusions.
    
    Args:
        filepath (str): Path to the document file.
        conclusions (dict): Extracted conclusions from the PMCF report.
    """
    doc = Document(filepath)
    for paragraph in doc.paragraphs:
        for key, value in conclusions.items():
            if key in paragraph.text:
                paragraph.text = paragraph.text.replace(key, value)
    doc.save(filepath)

def create_readme(output_folder, conclusions):
    """
    Creates a readme.txt with sections that need to be changed.
    
    Args:
        output_folder (str): Path to the output folder for updated documents.
        conclusions (dict): Extracted conclusions from the PMCF report.
    """
    readme_path = os.path.join(output_folder, "readme.txt")
    with open(readme_path, 'w') as readme_file:
        readme_file.write("Sections that need to be changed:\n")
        for key, value in conclusions.items():
            readme_file.write(f"{key}: {value}\n")
