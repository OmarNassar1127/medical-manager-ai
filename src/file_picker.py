import os

def file_picker(start_path=None):
    if start_path is None:
        start_path = os.path.expanduser("~")  # Start at the user's home directory by default
    current_path = start_path
    while True:
        print(f"\nCurrent Directory: {current_path}")
        items = os.listdir(current_path)
        items.insert(0, "..")  # Add option to go up one directory

        for idx, item in enumerate(items):
            print(f"{idx}: {item}")

        choice = input("Select a directory or file (number), or 'q' to quit: ")

        if choice.lower() == 'q':
            return None

        try:
            choice = int(choice)
            selected_item = items[choice]
            selected_path = os.path.join(current_path, selected_item)

            if os.path.isdir(selected_path):
                current_path = selected_path
            else:
                return selected_path
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
