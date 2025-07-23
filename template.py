import os

# Directories to create
directories = ['src', 'research']

# Files to create
files = [
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    '.env',
    'setup.py',
    'app.py',
    'research/trials.ipynb',
    'requirements.txt'
]

def create_structure():
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Create files
    for file_path in files:
        dir_name = os.path.dirname(file_path)
        if dir_name:  # Only make directory if there is one
            os.makedirs(dir_name, exist_ok=True)
        with open(file_path, 'w') as file:
            pass

    print("Directory and files created successfully!")

if __name__ == "__main__":
    create_structure()