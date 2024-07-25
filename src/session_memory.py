class SessionMemory:
    def __init__(self):
        self.memory = []

    def add_interaction(self, interaction):
        """
        Add a new interaction to the session memory.
        :param interaction: A dictionary containing details of the interaction.
        """
        self.memory.append(interaction)

    def get_memory(self):
        """
        Retrieve the current session memory.
        :return: A list of interactions stored in the session memory.
        """
        return self.memory

    def clear_memory(self):
        """
        Clear the session memory.
        """
        self.memory = []

# Example usage:
# session_memory = SessionMemory()
# session_memory.add_interaction({"user_input": "What is the prevalence of skin sensitization reactions?", "ai_response": "The prevalence is ..."})
# print(session_memory.get_memory())
