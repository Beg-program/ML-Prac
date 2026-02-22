# CSC 314 - File Operations Lifecycle Demonstration
# Author: Abiodun Toluwani Dorcas
# Matric No: 240805508
# Purpose: Demonstrate file open → write → read → close cycle 
#          and importance of proper resource management

def main():
    filename = "greetings.txt"
    message = "Hello World from CSC 314 file handling demo!\n"

    print("=== Starting file operation lifecycle demonstration ===\n")

    # Step 1: Writing to file (creation + write)
    try:
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(message)
            print(f"Successfully wrote message to '{filename}'")
            # File is automatically closed here when block ends
    except IOError as e:
        print(f"Error writing to file: {e}")
        return

    # Step 2: Reading from file (open + read)
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            content = file.read()
            print("\nContent read from file:")
            print("-" * 40)
            print(content.strip())   # remove trailing newline for clean display
            print("-" * 40)
            # File is automatically closed here
    except FileNotFoundError:
        print(f"File '{filename}' not found after writing!")
        return
    except IOError as e:
        print(f"Error reading file: {e}")
        return

    print("\nFile was successfully opened, written to, read from, and closed.")
    print("All resources were properly managed using 'with' statement.\n")


if __name__ == "__main__":
    main()