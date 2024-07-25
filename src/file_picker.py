import os

def file_picker(start_path=None):
    if start_path is None:
        start_path = os.path.expanduser("~")  # Start at the user's home directory by default
    current_path = start_path
    while True:
        print(f"\nCurrent Directory: {current_path}")
        items = sorted(os.listdir(current_path))  # Sort items for better user experience
        items.insert(0, "..")  # Add option to go up one directory
        items.append("Choose this folder")  # Add option to choose the current directory

        for idx, item in enumerate(items):
            print(f"{idx}: {item}")

        choice = input("Select a directory or file (number), or 'q' to quit: ")

        if choice.lower() == 'q':
            return None

        try:
            choice = int(choice)
            if choice == 0:  # If the choice is 0, go up one directory
                current_path = os.path.dirname(current_path)
            elif choice == len(items) - 1:  # If the choice is the last item, choose the current directory
                return current_path
            else:
                selected_item = items[choice]
                selected_path = os.path.join(current_path, selected_item)

                if os.path.isdir(selected_path):
                    current_path = selected_path
                else:
                    return selected_path
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
