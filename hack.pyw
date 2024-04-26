import os
import random
import string

# Specify the directory where you want to create the text files
base_directory = r"C:\Users\pranu\Desktop\Hello World"

# Function to generate random content
def generate_random_content(length):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + " ") for _ in range(length))

# Create 500 text files with random content
for i in range(1, 500):
    file_name = f"file_{i}.txt"
    file_path = os.path.join(base_directory, file_name)
    
    # Generate random content
    random_content = generate_random_content(random.randint(100,1000))
    
    # Write content to the file
    with open(file_path, 'w') as file:
        file.write(random_content)
    
    print(f"Created file: {file_path}")

print("Random text files creation complete.")
