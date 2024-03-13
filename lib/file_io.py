
# Function to write content to a file
def write_file(file_name, content):
    """Write content to a file."""

  
    with open(file_name, 'w') as f:
        # Write the provided content to the file
        f.write(content)

# Function to append content to a file
def append_file(file_name, content):
    """Append content to a file."""
    # Open the file in 'append' mode ('a') which will create the file if it doesn't exist,
   
    with open(file_name, 'a') as f:
        # Append the provided content to the file
        f.write(content)

# Function to read content from a file
def read_file(file_name):
    """Read content from a file."""
    
    with open(file_name, 'r') as f:
        # Read the content of the file and return it
        return f.read()
