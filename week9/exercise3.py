import os

def file_management():
    current_dir = os.getcwd()
    print(f" current directory: {current_dir}\n")
    folder_name = "lab_files"
    os.chdir(folder_name)
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    print(f"created folder name: {folder_name}")
    if os.path.exists(folder_name):
        print(f"folder exists, removing: {folder_name}")
        os.remove(folder_name)

    file_names = ["file1.txt, file2.txt", "file3.txt"]
    ls = []
    for file_name in file_names:
        ls.append(file_name)
    old_path = os.path.join(folder_name, "file1.txt")
    new_path = os.path.join(folder_name, "filehaidar.txt")

    print(f"\n=== Files after rename ===")
    files = os.listdir(folder_name)
    for file in files:
        print(f"- {file}")

    print(f"\n=== Cleaning up ===")
    for file in os.listdir(folder_name):
        file_path = os.path.join(folder_name, file)
    os.remove(file_path)
    print(f" file Deleted: {file}")


os.rmdir(folder_name)
print(f"removed folder : {folder_name}")

file_management()
