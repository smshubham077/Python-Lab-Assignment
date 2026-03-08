# Read from one text file and write its content to a new text file with the same content

# Read content from source file and write to destination file
source_file = input("Enter the source file name (with .txt extension): ")
dest_file = input("Enter the destination file name (with .txt extension): ")

try:
    with open(source_file, 'r') as src:
        content = src.read()
    
    with open(dest_file, 'w') as dst:
        dst.write(content)
    
    print("File copied successfully!")
except FileNotFoundError:
    print("Source file not found. Please check the file name and path.")
except Exception as e:
    print(f"An error occurred: {e}")
