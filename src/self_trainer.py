import random
from session_memory import SessionMemory

def train_ai(conclusions, session_memory: SessionMemory):
    """
    Trains the AI with the new data and implements a RAG status system.
    
    Args:
        conclusions (dict): Extracted conclusions from the PMCF report.
        session_memory (SessionMemory): Instance of SessionMemory to log interactions.
    """
    session_memory.add_interaction({"action": "train_ai", "input": conclusions})
    
    # Simulate training process
    print("Training AI with new data...")
    for key, value in conclusions.items():
        print(f"Training on conclusion: {key} -> {value}")
    
    # Implement RAG status system
    rag_status = {}
    for key in conclusions.keys():
        confidence_score = random.uniform(0, 1)
        if confidence_score < 0.33:
            rag_status[key] = "Red"
        elif confidence_score < 0.66:
            rag_status[key] = "Amber"
        else:
            rag_status[key] = "Green"
    
    # Print RAG status for review
    print("RAG Status for conclusions:")
    for key, status in rag_status.items():
        print(f"{key}: {status}")
    
    session_memory.add_interaction({"action": "train_ai", "output": rag_status})

    return rag_status
