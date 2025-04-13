import os
import shutil

# Define the directory to organize
source_directory = '/Users/APPLE/Desktop/Ak'  # Change this to your directory
organized_directory = os.path.join(source_directory, 'Organized')

# Create folders for organizing files
folders = ['Images', 'Documents', 'Others']
for folder in folders:
    os.makedirs(os.path.join(organized_directory, folder), exist_ok=True)

# Define file extensions for each category
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
}

# Organize files
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Determine the file type and move to the corresponding folder
    moved = False
    for category, extensions in file_categories.items():
        if any(filename.lower().endswith(ext) for ext in extensions):
            shutil.move(file_path, os.path.join(organized_directory, category, filename))
            moved = True
            print(f'Moved: {filename} to {category}')
            break

    # Move to 'Others' if no category matched
    if not moved:
        shutil.move(file_path, os.path.join(organized_directory, 'Others', filename))
        print(f'Moved: {filename} to Others')

print('Organization complete!')