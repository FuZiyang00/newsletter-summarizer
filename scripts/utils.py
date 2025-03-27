import sys
import time

def progressive_print(label, text, delay):
    """Prints text progressively with a delay, formatting it with indentation."""
    sys.stdout.write(label + "\n")  # Print the label and move to a new line
    sys.stdout.flush()
    
    # Process each line separately
    for line in text.split("\n"):
        sys.stdout.write("\t")  # Add tab before each line
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)  # Blocking delay for each character
        sys.stdout.write("\n")  # Move to the next line
        sys.stdout.flush()


