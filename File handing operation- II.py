# Ask user about source and destination file names. Print content of both files. Develop the application file handling script without comments.

source_file = input("Enter source file name: ")
dest_file = input("Enter destination file name: ")

try:
    with open(source_file, 'r') as f:
        src_content = f.read()
    print("Source file content:")
    print(src_content)
    print("-" * 40)
    
    with open(dest_file, 'w') as f:
        f.write(src_content)
    
    with open(dest_file, 'r') as f:
        dst_content = f.read()
    print("Destination file content:")
    print(dst_content)
    
    print("File handled successfully!")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(e)
